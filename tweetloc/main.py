# -*- coding: UTF-8 -*-

import urllib
import json
import os
import random
import time
import hmac
import binascii
import hashlib

# webapp2
from webapp2_extras import sessions
import webapp2
import logging

# requests
import requests
import requests_toolbelt.adapters.appengine
requests_toolbelt.adapters.appengine.monkeypatch()

# jinja2
import jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape'],
        autoescape=True)

# GAE app_id and callback_url
gae_app_id = 'api-proyecto-colaborativo'

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    # Production
    gae_callback_url = 'https://' + gae_app_id + '.appspot.com/oauth_callback'
else:
    # Local development server
    gae_callback_url = 'http://localhost:8080/oauth_callback'

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        """Crea un almacén de sesión para la petición actual. Permite mantener parámetros a través de las diferentes peticiones y almacena las cookies generadas que hayan usado la misma instancia de Session.

        """
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        """Devuelve la sesión previamente guardada y en la que se almacenan los parámetros necesarios para la aplicación.

        :return: Sesión previamente creada y guardada
        :rtype: Session
        """
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def isAuthorized(self):
        """Comprueba si los datos de la sesión son correctos.

        :return: Sesión correcta o fallida
        :rtype: bool
        """
        return 'oauth_token' in self.session \
            and 'oauth_token_secret' in self.session \
            and 'user_id' in self.session \
            and 'twitter_user' in self.session

config = {}
config['webapp2_extras.sessions'] = {'secret_key': 'my-super-secret-key'}

class MainHandler(BaseHandler):
    def get(self):
        """Define la retrollamada (callback) del MainHandler (manipulador). Si el usuario esta autorizado, muestra la pantalla principal. Si no es así, mostrará la pantalla de sesión no autorizada.

        :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
        :type BaseHandler: BaseHandler
        """
        # dependiendo de si existe una sessión autorizada
        # renderizamos un 'index' u otro
        if (self.isAuthorized()):
            # se ha añadido el nombre de usuario al objeto de sesión
            # para mostrarlo por pantalla
            datos = { 'twitter_user' : self.session['twitter_user'],
                        'firstlogin' : True }

            template = jinja_env.get_template("index_authorized.html")
            self.response.out.write(template.render(datos))

        else:
            template = jinja_env.get_template("index_unauthorized.html")
            self.response.out.write(template.render())

class SearchTweetsHandler(BaseHandler):
    def get(self):
        """Define la retrollamada (callback) del SearchTweetsHandler (manipulador). Gestiona la pagina web donde se realizan las busquedas de contenido en Twitter.

        :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
        :type BaseHandler: BaseHandler
        """
        # cargamos la plantilla
        template = jinja_env.get_template("index_authorized.html")

        # recogemos el parámetro 'query'
        q = self.request.get('query')

        if not q:
            self.redirect('/')
        else:        
            # preparamos la petición
            base_url = 'https://api.twitter.com/1.1/search/tweets.json'
            method = 'GET'
            try:
                oauth_token = self.session['oauth_token']
                oauth_token_secret = self.session['oauth_token_secret']

                oauth_headers = {'oauth_token': oauth_token}
                params = {'q' : q, 'count' : '100'}

                headers = {'User-Agent': 'Localizador de Tweets',
                        'Authorization': createAuthHeader(
                                method,
                                base_url,
                                oauth_headers,
                                params,
                                oauth_token_secret)
                        }

                # hacemos la petición
                response = requests.get(base_url + '?q=' + q + '&count=100', headers=headers)
           
            
            # si la respuesta es correcta, se renderizan los resultados 
                if (response.status_code == 200):
                    json_response = response.json()

                    tweets = []
                    for tweet in json_response['statuses']:
                        # se comprueba que existe la entrada 'place' en el diccionario del Tweet
                        if tweet['place']:
                            user = tweet['user']['name']
                            screen_name = tweet['user']['screen_name']
                            text = tweet['text']
                            location = tweet['place']
                            name = location['full_name']
                            
                            # si contiene la entrada 'place', es posible que contenga coordenadas precisas
                            # de la localización en 'coordinates' o 'geo' o que simplemente contenga
                            # el nombre del lugar desde el que se ha tuiteado en location['place']['full_name']
                            if tweet['coordinates']:
                                logging.debug('Place has coordinates: ' + str(tweet['coordinates']))
                                lon, lat = tweet['coordinates']['coordinates']

                            elif tweet['geo']:
                                logging.debug('Place has geo: ' + str(tweet['geo']))
                                lat, lon = tweet['geo']['coordinates']

                            # en este caso nos basaremos en el lugar para localizar el tweet
                            else:
                                lon, lat = None, None 
                        
                            # creamos un diccionario con los datos que nos interesan
                            data = {
                                'user' : user,
                                'screen_name' : screen_name,
                                'text' : text,
                                'location' : {
                                    'name' : name,
                                    'lat' : lat,
                                    'lon' : lon
                                }
                            }

                            tweets.append(data)

                    query = self.request.get('query')

                    # los datos que usaremos para crear el html de los resultados
                    # serán la query del usuario, el nombre de usuario y los tweets
                    datos = { 'query' : q,
                        'twitter_user' : self.session['twitter_user'],
                        'tweets' : tweets }

                    self.response.out.write(template.render(datos))

                # token invalido/caducado
                elif (response.status_code == 401):
                    logging.debug('Invalid tokens') 
                    self.redirect('/OAuthTwitterHandler')

                # error distinto
                else:   
                    logging.debug(response.status_code)
                    logging.debug('Unknown error')
                    self.redirect('/OAuthTwitterHandler')
            except KeyError:
                self.redirect('/OAuthTwitterHandler')

class OAuthTwitterHandler(BaseHandler):
    def get(self):
        """Redirige al usuario para iniciar la sesión en Twitter.

        :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
        :type BaseHandler: BaseHandler
        """
        # Step 1: Obtaining a request token
        method = 'POST'
        url = 'https://api.twitter.com/oauth/request_token'
        oauth_headers = {'oauth_callback': gae_callback_url}

        cabeceras = {'User-Agent': 'Localizador de Tweets',
                     'Authorization': createAuthHeader(method, url, oauth_headers, None, None)}
        respuesta = requests.post(url, headers=cabeceras)
        cuerpo = respuesta.text
        logging.info(cuerpo)

        # Your application should examine the HTTP status of the response.
        # Any value other than 200 indicates a failure.
        if respuesta.status_code != '200':
            logging.debug('/oauth/request_token != 200')

        # Your application should verify that oauth_callback_confirmed is true
        oauth_callback_confirmed = cuerpo.split('&')[2].replace('oauth_callback_confirmed=', '')

        if oauth_callback_confirmed != 'true':
            logging.debug('oauth_callback_confirmed != true')

        # and store the other two values
        self.session['oauth_token'] = cuerpo.split('&')[0].replace('oauth_token=', '')
        self.session['oauth_token_secret'] = cuerpo.split('&')[1].replace('oauth_token_secret=', '')

        # Step 2: Redirecting the user
        uri = "https://api.twitter.com/oauth/authenticate"
        params = {'oauth_token': self.session.get('oauth_token')}
        params_encoded = urllib.urlencode(params)
        self.redirect(uri + '?' + params_encoded)

class OAuthTwitterCallbackHandler(BaseHandler):
    def get(self):
        """Define la retrollamada (callback) de la API de Twitter.

        :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
        :type BaseHandler: BaseHandler
        """
        oauth_token = self.request.get("oauth_token")
        oauth_verifier = self.request.get("oauth_verifier")

        # Your application should verify that the token matches the request token received in step 1
        if oauth_token != self.session.get('oauth_token'):
            logging.debug('step2_oauth_token != step1_oauth_token')

        # Step 3: Converting the request token to an access token
        method = 'POST'
        url = 'https://api.twitter.com/oauth/access_token'
        oauth_headers = {'oauth_token': oauth_token}
        params = {'oauth_verifier': oauth_verifier}

        cabeceras = {'User-Agent': 'Localizador de Tweets',
                     'Content-Type': 'application/x-www-form-urlencoded',
                     'Authorization': createAuthHeader(method, url, oauth_headers, params,
                                                       self.session.get('oauth_token_secret'))}
        respuesta = requests.post(url, headers=cabeceras, data=params)
        cuerpo = respuesta.text

        self.session['oauth_token'] = cuerpo.split('&')[0].replace('oauth_token=', '')
        self.session['oauth_token_secret'] = cuerpo.split('&')[1].replace('oauth_token_secret=', '')
        self.session['user_id'] = cuerpo.split('&')[2].replace('user_id=', '')
        self.session['twitter_user'] = cuerpo.split('&')[3].replace('screen_name=', '')

        self.redirect('/')
        
def createAuthHeader(method, base_url, oauth_headers, request_params, oauth_token_secret):
    """Obtiene el token de autorización necesario para realizar peticiones a la API de Twitter.

    :param method: Tipo de petición HTTP
    :type method: str
    :param base_url: URL base de la petición
    :type base_url: str
    :param oauth_headers: Cabeceras HTTP para la autenticación
    :type oauth_headers: dict
    :param request_params: Parámetros de la petición
    :type request_params: dict
    :param oauth_token_secret: Token secreto para la autenticación
    :type oauth_token_secret: str
    :return: Token de autorización para peticiones futuras
    :rtype: str
    """
    oauth_nonce = str(random.randint(0, 999999999))
    oauth_signature_method = "HMAC-SHA1" 
    oauth_timestamp = str(int(time.time()))
    oauth_version = "1.0"

    oauth_headers.update({'oauth_consumer_key': os.environ.get('TWITTER_CONSUMER_KEY'),
                          'oauth_nonce': oauth_nonce,
                          'oauth_signature_method': oauth_signature_method,
                          'oauth_timestamp': oauth_timestamp,
                          'oauth_version': oauth_version})

    oauth_headers['oauth_signature'] = \
            urllib.quote(createRequestSignature(
                method,
                base_url,
                oauth_headers,
                request_params,
                oauth_token_secret),"")

    if oauth_headers.has_key('oauth_callback'):
        oauth_headers['oauth_callback'] = urllib.quote_plus(oauth_headers['oauth_callback'])

    authorization_header = "OAuth "

    for each in sorted(oauth_headers.keys()):
        if each == sorted(oauth_headers.keys())[-1]:
            authorization_header = authorization_header \
                                 + each + "=" + "\"" \
                                 + oauth_headers[each] + "\""
        else:
            authorization_header = authorization_header \
                                 + each + "=" + "\"" \
                                 + oauth_headers[each] + "\"" + ", "

    return authorization_header

def createRequestSignature(method, base_url, oauth_headers, request_params, oauth_token_secret):
    """Crea la firma para la autorización de la API de Twitter.

    :param method: Tipo de petición HTTP
    :type method: str
    :param base_url: URL base de la petición
    :type base_url: str
    :param oauth_headers: Cabeceras HTTP para la autenticación
    :type oauth_headers: dict
    :param request_params: Parámetros de la petición
    :type request_params: dict
    :param oauth_token_secret: Token secreto para la autenticación
    :type oauth_token_secret: str
    :return: Token de autorización para peticiones futuras
    :rtype: str
    """
    encoded_params = ''
    params = {}
    params.update(oauth_headers)
    if request_params:
        params.update(request_params)
    for each in sorted(params.keys()):
        key = urllib.quote(each, "")
        value = urllib.quote(params[each], "")
        if each == sorted(params.keys())[-1]:
            encoded_params = encoded_params + key + "=" + value
        else:
            encoded_params = encoded_params + key + "=" + value + "&"

    signature_base = method.upper() + \
                   "&" + urllib.quote(base_url, "") + \
                   "&" + urllib.quote(encoded_params, "")

    if oauth_token_secret == None:
        signing_key = urllib.quote(os.environ.get('TWITTER_CONSUMER_SECRET'), "") + "&"
    else:
        signing_key = urllib.quote(os.environ.get('TWITTER_CONSUMER_SECRET'), "") + "&" + urllib.quote(oauth_token_secret, "")

    hashed = hmac.new(signing_key, signature_base, hashlib.sha1)
    oauth_signature = binascii.b2a_base64(hashed.digest())

    return oauth_signature[:-1]

class LogoutHandler(BaseHandler):
    def get(self):
        """Define la retrollamada (callback) de la API de Twitter al cerrar sesión.

        :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
        :type BaseHandler: BaseHandler
        """
        self.session.clear()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/OAuthTwitterHandler', OAuthTwitterHandler),
    ('/oauth_callback', OAuthTwitterCallbackHandler),
    ('/search', SearchTweetsHandler),
    ('/cerrar_sesion', LogoutHandler),
], config=config, debug=True)

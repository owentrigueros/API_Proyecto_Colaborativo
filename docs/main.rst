.. _main:

API Reference
=============

Esta pagina contiene información sobre el modulo main de tweetloc.


:mod:`tweetloc.main` --- Twitter API wrapper
============================================

.. class:: BaseHandler(request=None, response=None)
   
   Esta clase provee la rutina necesaria para el 'manejador' base.

   :param request: libreria HTTP para gestionar peticiones
   :param response: libreria HTTP para gestionar respuestas


Metodos del BaseHandler
-----------------------

.. method:: dispatch()

   Crea un almacén de sesión para la petición actual. Permite mantener parámetros a través de las 
   diferentes peticiones y almacena las cookies generadas que hayan usado la misma instancia de Session.
   
   
.. method:: isAuthorized()

   Comprueba si los datos de la sesión son correctos.

   :return: Sesión correcta o fallida
   :rtype: bool
   

.. method:: session()

   Devuelve la sesión previamente guardada y en la que se almacenan los parámetros necesarios 
   para la aplicación.

   :return: Sesión previamente creada y guardada
   :rtype: Session
   
   
   
.. class:: MainHandler(request=None, response=None)

   Manipulador principal para la aplicación.
   
   :param BaseHandler: Manipulador base


Metodos del MainHandler
-----------------------

.. method:: get()

   Define la retrollamada (callback) del MainHandler (manipulador). Recibe un objeto (evento, 
   mensaje, etc) y actua en función del mismo. Si el usuario esta autorizado, muestra la 
   pantalla principal. Si no es así, mostrará la pantalla de sesión no autorizada.

   :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
   :type BaseHandler: BaseHandler



.. class:: SearchTweetsHandler(request=None, response=None)

   Manipulador para busqueda de tweets.
   
   :param BaseHandler: Manipulador base
   
   
Metodos del SearchTweetsHandler
-------------------------------

.. method:: get()

   Define la retrollamada (callback) del SearchTweetsHandler (manipulador). Gestiona la pagina web 
   donde se realizan las busquedas de contenido en Twitter.

   :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
   :type BaseHandler: BaseHandler



.. class:: OAuthTwitterHandler(request=None, response=None)

   Manipulador para autenticación de Twitter.
   
   :param BaseHandler: Manipulador base
   
   
Metodos del OAuthTwitterHandler
-------------------------------

.. method:: get()

   Redirige al usuario a la página oficial de Twitter para iniciar sesión.

   :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
   :type BaseHandler: BaseHandler
   
   

.. class:: OAuthTwitterCallbackHandler(request=None, response=None)

   Manipulador para gestión de respuesta de autenticación de Twitter.
   
   :param BaseHandler: Manipulador base
   
   
Metodos del OAuthTwitterCallbackHandler
---------------------------------------

.. method:: get()

   Define la retrollamada (callback) de la API de Twitter al iniciar sesión desde la página 
   oficial del servicio.

   :param BaseHandler: Clase base para todos los handler (manipuladores) registrados
   :type BaseHandler: BaseHandler
   
   
   
Metodo de createAuthHeader
--------------------------

.. method:: createAuthHeader(method, base_url, oauth_headers, request_params, oauth_token_secret)

   Obtiene el token de autorización necesario para realizar peticiones a la API de Twitter.
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
   


Metodo de createRequestSignature
--------------------------------

.. method:: createRequestSignature(method, base_url, oauth_headers, request_params, oauth_token_secret)

   Crea la firma para la autorización de la API de Twitter.
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
   


.. class:: LogoutHandler(request=None, response=None)
   
   Esta clase provee la rutina necesaria para el 'manejador' de cierre de sesión de Twitter.

   :param request: libreria HTTP para gestionar peticiones
   :param response: libreria HTTP para gestionar respuestas


Metodos del LogoutHandler
-------------------------

.. method:: get()

   Define la retrollamada (callback) de la API de Twitter al cerrar sesión. Recibe un objeto 
   (evento, mensaje, etc) y actua en función del mismo.
   

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
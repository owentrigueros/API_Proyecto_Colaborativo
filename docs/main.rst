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

   Crea un almacén de sesión para la petición actual. 
   Permite mantener parámetros a través de las diferentes 
   peticiones y almacena las cookies generadas que hayan 
   usado la misma instancia de Session.
   
   
.. method:: isAuthorized()

   Comprueba si los datos de la sesión son correctos.

   :rtype: Sesión correcta o fallida de la clase :class:`bool`
   

.. method:: session()

   Devuelve la sesión previamente guardada y en la que se 
   almacenan los parámetros necesarios para la aplicación.

   :rtype: Sesión previamente creada y guardada de la clase :class:`Session`

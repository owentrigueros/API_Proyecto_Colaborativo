.. _implic:

Implicaciones legales del proyecto
##################################

En este apartado se analizan los aspectos legales relacionados con el proyecto.

Reglamento Europeo de Protección de Datos
*****************************************

La aplicación utiliza un sistema de inicio de sesión para poder utilizar Twitter. Este sistema requiere que el usuario introduzca sus datos de Twitter para poder iniciar sesión. La *app*, en vez de guardar los datos de los usuarios, delega la resposabilidad directamente en Twitter. Se observa que la fase de inicio de sesión se realiza en una dirección propia de Twitter. Por lo tanto, la aplicación no guarda los datos de sus usuarios en ningún momento, solo los utiliza temporalmente para mostrarlos por pantalla.

La principal funcionalidad de la *app* es la de conseguir *tweets* que contengan palabras clave y ubicarlos en un mapa. En cuanto a los datos de los *tweets*, el programa simplemente recoge lo necesario para situarlos en el mapa y en ningún caso guarda registro alguno del histórico de *tweets* ni los datos que contenían. 

Por lo tanto, podemos afirmar que la aplicación cumple con las premisas del Reglamento Europeo de Protección de Datos puesto que muestra con total transparencia el uso que realiza de los datos y delega funcionalidades que trabajan con información sensible a los agentes que deberían tratarlos. En este caso, la empresa Twitter.

Ley de Servicios de la Sociedad de la Información y el Comercio Electrónico
***************************************************************************

La Ley de Servicios de la Sociedad de la Información y el Comercio Electrónico, obliga a que la web muestre un apartado de <<Aviso Legal>>. Como se ha mencionado anteriormente, la *app* delega la gestión de los datos a Twitter. La pantalla de inicio de sesión que proporciona Twitter, muestra de manera clara los permisos que va a utilizar y las implicaciones legales que conlleva aceptar los términos. En consecuencia, confirmamos que la *app* cumple la LSSI. 

Uso de Twitter para Desarrolladores
***********************************

Para el correcto funcionamiento de la *app*, es necesaria una cuenta de Desarrollador en Twitter. El uso de esta cuenta tiene que respetar ciertas políticas impuestas por Twitter. La aplicación tiene que respetar la política general de Twitter pero además, tiene ciertos requisitos. En el caso de esta *app*, se afirma que los datos recogidos desde Twitter no se utilizan con objetivo de lucrarse ni de realizar análisis alguno sobre los usuarios de Twitter. Este desarrollo se realiza con el objetivo de aprender a utilizar las herramientas y a gestionar un trabajo colaborativo por lo que cumple con las políticas exigidas por Twitter.

Licencias Software
******************

El código y la documentación de este proyecto utilizan la licencia MIT. Esta licencia permite modificar, distribuir y utilizarlo tanto para uso personal como para uso comercial siempre y cuando se indique de manera adecuada el *copyright*. A su vez, la aplicación utiliza herramientas que utilizan otros tipos de licencias software. 

El código Python, por ejemplo, utiliza una licencia muy permisiva. Permite el uso de Python para cualquier fin siempre y cuando se acepten los términos de uso de Python. A diferencia de algunas licencias de código abierto, Python no obliga a publicar las modificaciones realizadas utilizando el lenguaje Python. 

Dado que el código fuente de la *app* es público y que no se utiliza con el objetivo de lucrarse, podemos afirmar que la implementacion respeta todas las licencias exigidas por las librerías utilizadas.

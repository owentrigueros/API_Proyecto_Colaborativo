# Intrucciones para crear la documentación
A continuación se describe cómo preparar el entorno virtual necesario para la generación de la documentación, cómo inicializar la documentación y cómo generarla/actualizarla.

## Crear entorno virtual
Para que el gestor de documentación parsee correctamente el código (y, opcionalmente, ejecute los tests del mismo) es necesario crear un entorno que satisfaga las dependencias del proyecto (no confundir con la carpeta `lib/`, que se utiliza en el despliege).

    python2 -m virtualenv -p /usr/bin/python2.7 venv
    source venv/bin/activate
    pip install -r requirements/docs.txt

## Inicializar documentacion
(Este paso sólo ha tenido que hacerse una vez, está sin completar porque no es prioritario.)

En la raíz del proyecto, se crea la carpeta `docs/` y se entra en la misma.

    mkdir docs
    cd docs/

Desde ahí, se ejecuta el siguiente comando para crear los ficheros necesarios para Sphinx, la herramienta que se utiliza para gestionar la documentación.

    sphinx-quickstart

Ha sido necesario configurar Sphinx modificando `conf.py`.

    vim conf.py 

## Generar/Actualizar la documentación

### Generación automática de documentación del código
Después de haber hecho cambios en el código, se genera la documentación de manera automática con `sphinx-apidoc` (internamente, hace uso de las `docstrings` del código para generarla):

    cd docs/
    sphinx-apidoc -o source/ ../tweetloc/ -f

### Escribir documentación
La documentación se escribe en un lenguaje que extiende a Markdown, llamado reStructuredText. Para tener una referencia de cómo añadir nuevas secciones, echad un vistazo a los ficheros `docs/index.rst` y `docs/test.rst`.

Una vez se hayan realizado cambios y se desee regenerar, por ejemplo, la documentación en formato HTML, se debe ejecutar este comando (dentro de `docs/`):

    make html

El output se encontrará en la carpeta `_build/html`.

# API Proyecto Colaborativo
Proyecto colaborativo de la asignatura "Aspectos Profesionales de la Informática" del Grado de Ingeniería Informática de Gestión y Sistemas de Información de la UPV/EHU.

## Instalar dependencias
Instalar dependencias con pip (Python 2.7) en la carpeta `lib/`:

`python2 -m pip install -t lib/ -r requirements.txt`

## Instalación, configuración y despliege del proyecto
A continuación, se indica cómo instalar Google Cloud SDK, cómo configurarlo para trabajar con el proyecto y, finalmente, como realizar el despliege de la aplicación en Google Cloud.

### Instalación de Google Cloud SDK
- Arch Linux:

`yay -S google-cloud-sdk`

- Ubuntu:

Añadir la URI de distribución de Google Cloud SDK como una nueva fuente:

`echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list`

Importar la clave pública de Google Cloud Platform:

`curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -`

Actualizar la lista de paquetes e instalar `google-cloud-sdk`:

`sudo apt-get update && sudo apt-get install google-cloud-sdk`

### Configuración del proyecto

Identificarse en Google App Engine:

`gcloud auth login`

Ir al directorio en el que se encuentra el proyecto y configurar Google Cloud SDK para que trabaje con el mismo:

`gcloud config set project api-proyecto-colaborativo`

### Despliege
Para subir o actualizar la aplicación, ejecutar:

`gcloud app deploy`

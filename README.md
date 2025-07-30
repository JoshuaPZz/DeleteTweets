🧹 DeleteTweet - Elimina tus tweets automáticamente
Este proyecto te permite eliminar en masa tus tweets antiguos de forma segura usando la API de Twitter v1.1 y autenticación OAuth 1.0a.
Es ideal si descargaste tu historial desde Twitter y quieres limpiar tu cuenta en base a criterios como la fecha.

📁 Estructura del proyecto
bash
Copiar
Editar
DeleteTweet/
├── delete_tweets.py
├── conf/
│   └── config.yaml         # Tus credenciales de Twitter
├── tweet-headers.js        # Archivo exportado desde Twitter
├── README.md
✅ Requisitos
Python 3.8 o superior

Cuenta de desarrollador en Twitter

Acceso a tu archivo de datos descargado de Twitter

🚀 ¿Qué hace este script?
Lee el archivo tweet-headers.js de tu exportación de datos de Twitter.

Elimina automáticamente los tweets más antiguos que cierta fecha (puedes cambiarla).

Filtra solo tweets originales (no elimina retweets por defecto).

🛠️ Instalación
Clona este repositorio:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/DeleteTweet.git
cd DeleteTweet
Crea un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instala las dependencias:

bash
Copiar
Editar
pip install tweepy hydra-core
🔐 Cómo obtener tus credenciales de Twitter
Paso 1: Crear una App en Twitter Developer
Ve a https://developer.twitter.com/en/portal/dashboard

Crea un nuevo proyecto + app si aún no tienes uno.

En el menú de tu app, entra a "User authentication settings"

Activa:

OAuth 1.0a

Permisos: selecciona Read and Write

Callback URL: puedes usar http://localhost/

Guarda los cambios.

Paso 2: Obtener las claves
Ve a la pestaña Keys and tokens

Copia los siguientes valores:

API Key

API Key Secret

Access Token

Access Token Secret

🔧 Configuración
Crea el archivo conf/config.yaml (o edita el que viene con el proyecto):

yaml
Copiar
Editar
# conf/config.yaml

twitter:
  api_key: "TU_API_KEY"
  api_secret: "TU_API_SECRET"
  access_token: "TU_ACCESS_TOKEN"
  access_token_secret: "TU_ACCESS_TOKEN_SECRET"
📥 Obtener tu archivo tweet-headers.js
Entra a https://twitter.com/settings/download_your_data

Solicita tus datos y espera el correo de Twitter.

Descarga y descomprime el archivo .zip.

Dentro de la carpeta data/, copia el archivo tweet-headers.js al directorio raíz de este proyecto.

▶️ Ejecutar el script
Una vez configurado todo:

bash
Copiar
Editar
python delete_tweets.py
El script buscará los tweets en tweet-headers.js, evaluará sus fechas y eliminará los que cumplan los filtros.

⚙️ Personalización
En delete_tweets.py puedes cambiar esta línea para modificar la fecha límite:

python
Copiar
Editar
cutoff_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
Solo se eliminarán los tweets anteriores a esa fecha.

❗ Advertencia
No se puede deshacer: asegúrate de hacer un respaldo completo antes de ejecutar este script.

Este script no elimina retweets por defecto. Puedes modificar esa lógica si lo necesitas.

📄 Licencia
MIT License.
Puedes usar y modificar este script libremente, pero bajo tu propia responsabilidad.

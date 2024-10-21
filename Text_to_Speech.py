# %% [markdown]
# # 1. Preparación de Entorno

# %%
from dotenv import load_dotenv

import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

bucket = "datasetsaudio"

# Utilitario para manifrompular los servicios de AWS
import boto3

# %%
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_DEFAULT_REGION")

# %% [markdown]
# # 2. Conexión al servicio

# %%
# Obtenemos el cliente de servicio
polly = boto3.client(
    "polly",  # Servicio al que nos conectamos
    aws_access_key_id=access_key_id,  # Identificador de la clave
    aws_secret_access_key=secret_access_key,  # Contraseña de la clave
    region_name=region,  # Región de la clave
)

# %% [markdown]
# # 3. Envío de consulta

# %%
# Texto que se leerá
texto = (
    "Bienvenido al Taller sobre Texto a Voz  Utilizando  la herramienta de Amazon Polly"
)

# %%
# Definimos el idioma de la voz
# La lista completa de idiomas se encuentra disponible desde:
# https://docs.aws.amazon.com/es_es/polly/latest/dg/SupportedLanguage.html
idioma = "es-US"

# %%
voz = "Miguel"

# %%
engine = "standard"

# %%
formatoDeAudio = "pcm"

# %%
# Enviamos la consulta
respuesta = polly.synthesize_speech(
    Text=texto,  # Texto que se leerá
    OutputFormat=formatoDeAudio,  # Formato del audio
    VoiceId=voz,  # Voz que leerá el audio
    Engine=engine,
)

# %% [markdown]
# # 4. Extracción del audio

# %%
# Leemos el audio desde la respuesta
audio = respuesta["AudioStream"].read()

# %%
# Librería para manipular archivos WAV
import wave

# %%
# Con el utilitario "wave" abrimos el archivo en modo "escritura binaria"
with wave.open("./content/texto_a_voz.wav", "wb") as archivo:
    # Configuramos el archivo para guardar el audio en "Mono" (1)
    archivo.setnchannels(1)

    # Configuramos el archivo para guardar el audio en 16 bits (2)
    archivo.setsampwidth(2)

    # Configuramos el archivo para una frecuencia de 16 kHz
    archivo.setframerate(16000)

    # Escribimos el archivo
    archivo.writeframes(audio)

# %%
# Utilitario para escuchar un audio
from IPython.display import Audio

# %%
# Reproducimos el audio
Audio("./content/texto_a_voz.wav")

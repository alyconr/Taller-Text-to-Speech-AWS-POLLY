# Taller de Text-to-Speech con Amazon Polly

## Tabla de Contenidos

1.  [Introducción](#introducci%C3%B3n)
2.  [Preparación del Entorno](#preparaci%C3%B3n-del-entorno)
3.  [Conexión al Servicio](#conexi%C3%B3n-al-servicio)
4.  [Envío de Consulta](#env%C3%ADo-de-consulta)
5.  [Extracción del Audio](#extracci%C3%B3n-del-audio)
6.  [Conclusión](#conclusi%C3%B3n)

## Introducción

Amazon Polly es un servicio de Text-to-Speech (TTS) que utiliza tecnologías avanzadas de aprendizaje profundo para sintetizar voz natural a partir de texto. Este taller se centra en cómo utilizar Amazon Polly para convertir texto en audio realista.

Amazon Polly ofrece una amplia gama de voces en varios idiomas y acentos, permitiendo a los desarrolladores elegir la voz más adecuada para sus aplicaciones. Además, Polly proporciona diferentes tipos de voces, incluyendo voces neuronales que ofrecen una calidad de sonido aún más natural y expresiva.

## Preparación del Entorno

Para comenzar, necesitamos configurar nuestro entorno de trabajo:

```python
from dotenv import load_dotenv
import os
import boto3

# Carga las variables de entorno desde el archivo .env
load_dotenv()

bucket = "datasetsaudio"

# Configuración de las credenciales de AWS
access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION')
```

En este paso, cargamos las variables de entorno necesarias para autenticar nuestra conexión con AWS. Asegúrate de tener un archivo `.env` con tus credenciales de AWS.

## Conexión al Servicio

Una vez que tenemos nuestras credenciales, podemos conectarnos al servicio de Amazon Polly:

```python
polly = boto3.client(
  "polly",
  aws_access_key_id = access_key_id,
  aws_secret_access_key = secret_access_key,
  region_name = region
)
```

Este código crea un cliente de Amazon Polly que utilizaremos para interactuar con el servicio.

## Envío de Consulta

Ahora que estamos conectados, podemos enviar una consulta para sintetizar voz:

```python
texto = "Bienvenido al Taller sobre Texto a Voz Utilizando la herramienta de Amazon Polly"
idioma = "es-US"
voz = "Miguel"
engine = "standard"
formatoDeAudio = "pcm"

respuesta = polly.synthesize_speech(
    Text = texto,
    OutputFormat = formatoDeAudio,
    VoiceId = voz,
    Engine = engine
)
```

En este paso, definimos el texto que queremos convertir a voz, el idioma, la voz específica que queremos usar, el motor de síntesis y el formato de audio deseado. Luego, enviamos esta información a Amazon Polly para su procesamiento.

## Extracción del Audio

Una vez que recibimos la respuesta de Amazon Polly, podemos extraer y guardar el audio:

```python
import wave

audio = respuesta["AudioStream"].read()

with wave.open("./content/texto_a_voz.wav", 'wb') as archivo:
    archivo.setnchannels(1)
    archivo.setsampwidth(2)
    archivo.setframerate(16000)
    archivo.writeframes(audio)

# Para reproducir el audio (en un entorno Jupyter Notebook)
from IPython.display import Audio
Audio("./content/texto_a_voz.wav")
```

Este código guarda el audio sintetizado como un archivo WAV y, si estás en un entorno Jupyter Notebook, te permite reproducirlo directamente.

## Conclusión

En este taller, hemos aprendido cómo utilizar Amazon Polly para convertir texto en voz. Comenzamos configurando nuestro entorno y conectándonos al servicio de AWS. Luego, enviamos una consulta para sintetizar voz a partir de un texto dado, especificando parámetros como el idioma y la voz deseada. Finalmente, extrajimos el audio resultante y lo guardamos como un archivo WAV.

Amazon Polly ofrece una solución robusta y flexible para la síntesis de voz, permitiendo a los desarrolladores integrar capacidades de texto a voz de alta calidad en sus aplicaciones. Con una amplia variedad de voces e idiomas disponibles, Polly se adapta a diversas necesidades y casos de uso, desde la creación de contenido accesible hasta el desarrollo de interfaces de voz naturales.

Este taller proporciona una base sólida para comenzar a trabajar con Amazon Polly. A medida que explores más a fondo, podrás descubrir características avanzadas como el ajuste de la velocidad del habla, la entonación y el uso de marcas de voz para un control aún más preciso sobre la salida de audio.

## Autores

Este taller fue desarrollado por:

- Jeysson Aly Contreras
  - LinkedIn: [https://www.linkedin.com/in/jeysson-aly-contreras/](https://www.linkedin.com/in/jeysson-aly-contreras/)
  - GitHub: [https://github.com/alyconr](https://github.com/alyconr)

Si tienes preguntas sobre este taller o estás interesado en colaborar en proyectos similares, no dudes en conectarte a través de LinkedIn o revisar mis proyectos en GitHub.

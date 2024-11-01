
# Generador de Conciencia Visual

## Descripción
Este proyecto es un **Generador de Conciencia Visual** que crea imágenes impactantes sobre el cambio climático. El objetivo es sensibilizar al público sobre los efectos y las causas de esta crisis global mediante imágenes informativas y visuales atractivos que se pueden compartir en redes sociales o utilizar en plataformas de concienciación.

## Objetivo
Crear y difundir imágenes que ayuden a comprender los desafíos ambientales actuales y fomenten acciones positivas para el planeta, utilizando datos curiosos, mensajes variados y estadísticas relevantes sobre el cambio climático.

## Requisitos
- **Python 3.x**
- **Bibliotecas**:
  - `discord.py` (para la funcionalidad del bot en Discord)
  - `Pillow` (para manipular y crear imágenes)
  - `matplotlib` (para generar gráficos y visualizaciones de datos)

Para instalar las dependencias, usa el siguiente comando:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto
- **bot.py**: Archivo principal que define el bot de Discord y sus comandos.
- **main.py**: Contiene la lógica para generar las imágenes de conciencia climática.
- **images/**: Carpeta donde se guardan las imágenes generadas.
- **docs/**: Documentación adicional y recursos del proyecto.

## Comandos del Bot en Discord
- `!conciencia <color de fondo> <color de texto>`: Genera una imagen con un mensaje aleatorio sobre el cambio climático. Ejemplo: `!conciencia yellow blue`
- `!estadisticas`: Muestra estadísticas generales sobre el cambio climático.
- `!recursos`: Muestra enlaces a recursos confiables sobre el cambio climático.
- `!ayuda`: Lista todos los comandos disponibles y sus descripciones.

## Ejecución del Bot
Para ejecutar el bot, asegúrate de tener configurado un bot en el [Discord Developer Portal](https://discord.com/developers/applications) y reemplaza `YOUR_BOT_TOKEN` en `bot.py` con tu token de bot real. Luego, inicia el bot con:

```bash
python bot.py
```

## Ejemplo de Uso
1. Ejecuta el bot en Discord.
2. Usa el comando `!conciencia` con colores personalizados, como `!conciencia green white`.
3. Observa cómo el bot genera y envía una imagen con un mensaje de conciencia climática.

## Mensajes de Conciencia Climática
El bot utiliza una lista de mensajes y datos curiosos en español para variar el contenido y proporcionar información interesante sobre el cambio climático, tales como:
- "Actúa ahora para salvar nuestro planeta!"
- "Cada acción cuenta, ¡haz tu parte!"
- "¿Sabías que el 2020 fue uno de los años más cálidos registrados?"
- "La Tierra nos necesita más que nunca."

Estos mensajes se eligen aleatoriamente cada vez que se ejecuta el comando `!conciencia`.

## Referencias útiles
1. [Documentación de Pillow](https://pillow.readthedocs.io/): Guía oficial para aprender a usar la biblioteca de manipulación de imágenes.
2. [Documentación de Matplotlib](https://matplotlib.org/stable/contents.html): Referencia para crear gráficos en Python.
3. [Documentación de discord.py](https://discordpy.readthedocs.io/): Referencia para desarrollar bots en Discord.

## Recursos sobre el Cambio Climático
1. [ONU - Acción por el Clima](https://www.un.org/es/climatechange): Información y contexto sobre la acción climática global.
2. [NASA - Cambio Climático y Medioambiente](https://climate.nasa.gov/): Datos actualizados sobre el cambio climático y sus efectos.
3. [IPCC - Panel Intergubernamental sobre Cambio Climático](https://www.ipcc.ch/): Informes y datos científicos sobre el cambio climático.

---

Este README proporciona una guía completa del proyecto, incluyendo los objetivos, comandos, estructura, y referencias útiles para la investigación y desarrollo del bot de conciencia climática.

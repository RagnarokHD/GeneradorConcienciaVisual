import discord
from discord.ext import commands
import os
import random
from main import create_advanced_image  # Importa la función desde tu código existente

# Configura el bot y sus intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de mensajes y datos curiosos sobre el cambio climático en español
climate_messages = [
    "¡Actúa ahora para salvar nuestro planeta!",
    "Reduce, reutiliza, recicla para un mundo mejor.",
    "Cada acción cuenta, ¡haz tu parte!",
    "La Tierra nos necesita más que nunca.",
    "El cambio climático es real y urgente.",
    "¿Sabías que el 2020 fue uno de los años más cálidos registrados?",
    "Cada año se pierden millones de hectáreas de bosque, ¡protejámoslas!",
    "El nivel del mar ha aumentado aproximadamente 20 cm desde 1880.",
    "Las emisiones de CO₂ alcanzan niveles récord cada año.",
    "La energía renovable es el futuro para frenar el calentamiento global.",
    "Pequeños cambios en tu vida diaria pueden tener un gran impacto en el planeta.",
    "¿Sabías que el 70% de las especies podrían extinguirse debido al cambio climático?",
    "La temperatura global ha aumentado alrededor de 1.2°C desde la era preindustrial.",
    "¡Tu esfuerzo por reducir el uso de plásticos puede marcar la diferencia!",
    "El cambio climático afecta directamente a la biodiversidad, ¡cuidémosla!"
]

# Comando para generar una imagen de conciencia climática con un mensaje aleatorio en español
@bot.command(name="conciencia")
async def generate_awareness_image(ctx, fondo="lightblue", texto="darkgreen"):
    # Selecciona un mensaje aleatorio
    message = random.choice(climate_messages)
    
    # Genera la imagen usando el código existente y parámetros personalizados
    create_advanced_image(
        text=message,
        bg_color=fondo,
        text_color=texto,
        add_graph=True,
        add_logo=False  # Cambia a True si tienes un logotipo disponible
    )
    
    # Envía la imagen generada al canal de Discord
    image_path = max([f"images/{file}" for file in os.listdir("images")], key=os.path.getctime)
    await ctx.send(file=discord.File(image_path))

# Comando para mostrar estadísticas sobre el cambio climático en español
@bot.command(name="estadisticas")
async def climate_statistics(ctx):
    stats_message = (
        "**Estadísticas sobre el Cambio Climático**\n"
        "- La temperatura global ha aumentado aproximadamente 1.2°C desde la era preindustrial.\n"
        "- Cada año, se emiten alrededor de 36 mil millones de toneladas de CO₂ a la atmósfera.\n"
        "- El nivel del mar ha subido cerca de 20 cm desde 1880.\n"
    )
    await ctx.send(stats_message)

# Comando para mostrar recursos confiables sobre el cambio climático en español
@bot.command(name="recursos")
async def climate_resources(ctx):
    resources_message = (
        "**Recursos sobre el Cambio Climático**\n"
        "- [ONU - Acción por el Clima](https://www.un.org/es/climatechange)\n"
        "- [NASA - Cambio Climático y Medioambiente](https://climate.nasa.gov/)\n"
        "- [IPCC - Panel Intergubernamental sobre Cambio Climático](https://www.ipcc.ch/)\n"
    )
    await ctx.send(resources_message)

# Comando de ayuda en español
@bot.command(name="ayuda")
async def help_command(ctx):
    help_message = (
        "**Comandos Disponibles:**\n"
        "- `!conciencia <color de fondo> <color de texto>`: Genera una imagen con un mensaje aleatorio sobre el cambio climático. Ejemplo: `!conciencia yellow blue`\n"
        "- `!estadisticas`: Muestra estadísticas generales sobre el cambio climático.\n"
        "- `!recursos`: Muestra enlaces a recursos confiables sobre el cambio climático.\n"
        "- `!ayuda`: Muestra esta lista de comandos."
    )
    await ctx.send(help_message)

# Evento para avisar cuando el bot esté listo
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# Ejecuta el bot (reemplaza 'YOUR_BOT_TOKEN' con tu token real)
bot.run("YOUR_BOT_TOKEN")

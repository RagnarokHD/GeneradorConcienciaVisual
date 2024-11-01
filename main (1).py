import os
import random
import datetime
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def get_random_message():
    messages = [
        "Act Now to Save Our Planet!",
        "Reduce, Reuse, Recycle!",
        "Every Action Counts!",
        "The Earth Needs Us!",
        "Climate Change is Real!"
    ]
    return random.choice(messages)

def save_image_with_timestamp(image, base_name="climate_message"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = f"images/{base_name}_{timestamp}.png"
    image.save(image_path)
    print(f"Image saved to {image_path}")

def add_graph_to_image(base_image, width, height):
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Temperatura")
    ax.legend()
    plt.savefig("images/temp_graph.png", bbox_inches='tight', transparent=True)
    plt.close(fig)
    
    graph_image = Image.open("images/temp_graph.png").resize((200, 150))
    base_image.paste(graph_image, (width - 220, 20), graph_image)
    os.remove("images/temp_graph.png")
    return base_image

def create_advanced_image(text=None, width=800, height=400, bg_color="lightblue", text_color="darkgreen", font_path="arial.ttf", add_graph=False, add_logo=False):
    if text is None:
        text = get_random_message()
    
    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    font_size = 40
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Obtener el tamaño del texto y centrarlo en la imagen
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(text_position, text, fill=text_color, font=font)
    
    os.makedirs("images", exist_ok=True)
    
    if add_graph:
        image = add_graph_to_image(image, width, height)
    
    if add_logo:
        logo = Image.open("path_to_logo.png").resize((100, 100))
        image.paste(logo, (width - 120, height - 120), logo)

    save_image_with_timestamp(image)

if __name__ == "__main__":
    create_advanced_image(
        text="Protect Our Future!",
        bg_color="lightblue",
        text_color="darkgreen",
        add_graph=True,
        add_logo=False  # Cambia a True si tienes un logotipo disponible
    )

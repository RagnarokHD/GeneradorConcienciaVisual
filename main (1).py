
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Function to create a basic image with a message about climate change
def create_image_with_text(text):
    # Define image size and color
    width, height = 800, 400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Text settings
    font_size = 40
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        
    # Define text position and color
    text_position = (50, height // 2 - font_size)
    text_color = "black"
    
    # Add text to the image
    draw.text(text_position, text, fill=text_color, font=font)
    
    # Save image
    image.save("images/climate_message.png")
    print("Image saved to images/climate_message.png")

# Example usage
if __name__ == "__main__":
    create_image_with_text("Act Now to Save Our Planet!")

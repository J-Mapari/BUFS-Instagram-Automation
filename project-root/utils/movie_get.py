from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Function to calculate luminance of a color
def get_luminance(color):
    r, g, b = [int(color[i:i+2], 16) for i in (1, 3, 5)]  # Convert hex to RGB
    return 0.299 * r + 0.587 * g + 0.114 * b  # Luminance formula

def generate_images(movie_details):
    # Download the movie poster
    response = requests.get(movie_details["poster_url"])

    # Check if the response is successful (status code 200)
    if response.status_code != 200:
        print(f"Failed to retrieve image. Status code: {response.status_code}")
        return
    
    try:
        # Try to open the image from the response content
        poster = Image.open(BytesIO(response.content)).resize((468, 667))  # Resized to match dimensions
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Define color palettes
    color_palettes = [
        {"bg_color": "#2D572C", "title_bar_color": "#A9A9A9", "text_color": "#FFA500"},
        {"bg_color": "#1C1C1C", "title_bar_color": "#F1C40F", "text_color": "#ECF0F1"},
        {"bg_color": "#2C3E50", "title_bar_color": "#E74C3C", "text_color": "#FFFFFF"},
        {"bg_color": "#8E44AD", "title_bar_color": "#F39C12", "text_color": "#E0E0E0"},
        {"bg_color": "#16A085", "title_bar_color": "#1ABC9C", "text_color": "#FFFFFF"},
        {"bg_color": "#FF6347", "title_bar_color": "#FF4500", "text_color": "#F5FFFA"},
        {"bg_color": "#34495E", "title_bar_color": "#2ECC71", "text_color": "#000000"},
        {"bg_color": "#E74C3C", "title_bar_color": "#16A085", "text_color": "#F9E79F"}
    ]
    
    # Fonts
    title_font = ImageFont.truetype(r"C:\JANMEIJAY\UOB\actually personal\BUFS-Instagram-Automation\project-root\utils\PassionOne-Regular.ttf", 150)  # Update path as needed

    # Function to add text with shadow effect
    def draw_text_with_shadow(draw, text, position, font, text_color, shadow_color, shadow_offset=(5, 5)):
        x, y = position
        shadow_offset_x, shadow_offset_y = shadow_offset
        # Draw the shadow by drawing the text with a shadow color
        draw.text((x + shadow_offset_x, y + shadow_offset_y), text, font=font, fill=shadow_color)
        # Draw the main text on top of the shadow
        draw.text((x, y), text, font=font, fill=text_color)

    # Loop through each palette and generate an image
    for idx, palette in enumerate(color_palettes, 1):
        bg_color = palette["bg_color"]
        title_bar_color = palette["title_bar_color"]
        text_color = palette["text_color"]

        # Create the image canvas
        img = Image.new("RGB", (1080, 1080), bg_color)
        draw = ImageDraw.Draw(img)

        # Add the title bar
        draw.rectangle([(51.5, 42.7), (1031.6, 231.5)], fill=title_bar_color)
        
        # Add the movie title with shadow
        title_text = movie_details["title"].upper()
        
        # Use textbbox to get the size of the text
        bbox = draw.textbbox((0, 0), title_text, font=title_font)
        title_width, title_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        title_x = (1080 - title_width) // 2
        title_y = 43 + (195 - title_height) // 2 - 30  # Move the title up by 30 pixels
        draw_text_with_shadow(draw, title_text, (title_x, title_y), title_font, text_color, "black")

        # Add the circles around the title bar
        circle_radius = title_width // 4  # Half the diameter of the title bar width
        top_circle_center = (title_x - circle_radius - 20, 42 + (195 // 2))  # Left side circle
        bottom_circle_center = (title_x + title_width + circle_radius + 20, 42 + (195 // 2))  # Right side circle

        # Draw two circles with the same background color as the canvas
        draw.ellipse([top_circle_center[0] - circle_radius, top_circle_center[1] - circle_radius,
                      top_circle_center[0] + circle_radius, top_circle_center[1] + circle_radius], 
                     fill=bg_color, outline=bg_color)

        draw.ellipse([bottom_circle_center[0] - circle_radius, bottom_circle_center[1] - circle_radius,
                      bottom_circle_center[0] + circle_radius, bottom_circle_center[1] + circle_radius], 
                     fill=bg_color, outline=bg_color)

        # Show the image
        img.show()

        # Optionally, save the image
        img.save(f"movie_poster_title_with_circles_{idx}.png")

# Example usage:
movie_details = {
    "title": "Oppenheimer",
    "poster_url": "https://m.media-amazon.com/images/I/71xDtUSyAKL._AC_UF894,1000_QL80_.jpg"  # Replace with your actual poster URL
}
generate_images(movie_details)

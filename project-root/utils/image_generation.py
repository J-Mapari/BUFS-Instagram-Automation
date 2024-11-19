from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def generate_images(movie_details, venue, time):
    # Download the movie poster
    response = requests.get(movie_details["poster_url"])
    poster = Image.open(BytesIO(response.content)).resize((450, 650))

    # Fonts
    title_font = ImageFont.truetype("arial.ttf", 60)  # Replace with your font file
    text_font = ImageFont.truetype("arial.ttf", 40)
    small_font = ImageFont.truetype("arial.ttf", 30)

    # Background color
    bg_color = "#556B2F"  # Olive green
    text_color = "black"

    # Image 1: Poster with venue and time
    img1 = Image.new("RGB", (1080, 1080), bg_color)
    draw = ImageDraw.Draw(img1)

    # Add the title
    draw.text((50, 30), movie_details["title"].upper(), fill="black", font=title_font)

    # Paste the poster
    img1.paste(poster, (50, 100))

    # Add text for Date, Location, and Time
    draw.text((550, 100), f"DATE :\nMonday 18 November, 2024", fill=text_color, font=text_font, spacing=10)
    draw.text((550, 300), f"LOCATION :\n{venue}", fill=text_color, font=text_font, spacing=10)
    draw.text((550, 500), f"TIME :\n{time}", fill=text_color, font=text_font, spacing=10)

    # Add Instagram handle
    draw.text((850, 1000), "@BATHFILMSOC", fill="black", font=small_font)

    # Save the first image
    img1_path = "static/images/post1.jpg"
    img1.save(img1_path)

    # Image 2: Title, year, director, and description with actor photos
    img2 = Image.new("RGB", (1080, 1080), bg_color)
    draw = ImageDraw.Draw(img2)

    # Add the title and director info
    draw.text((50, 30), movie_details["title"].upper(), fill="black", font=title_font)
    draw.text((50, 150), f"[{movie_details['year']}] dir. {movie_details['director']}", fill=text_color, font=text_font)

    # Add the description
    description = movie_details["description"]
    draw.text((50, 300), description, fill=text_color, font=small_font, spacing=10)

    # Download actor images (replace with actual actor URLs)
    actor1_url = "https://via.placeholder.com/450"  # Replace with actor 1's photo URL
    actor2_url = "https://via.placeholder.com/450"  # Replace with actor 2's photo URL

    actor1 = Image.open(BytesIO(requests.get(actor1_url).content)).resize((450, 250))
    actor2 = Image.open(BytesIO(requests.get(actor2_url).content)).resize((450, 250))

    # Paste actor images
    img2.paste(actor1, (50, 500))
    img2.paste(actor2, (550, 500))

    # Add Instagram handle
    draw.text((850, 1000), "@BATHFILMSOC", fill="black", font=small_font)

    # Save the second image
    img2_path = "static/images/post2.jpg"
    img2.save(img2_path)

    return [img1_path, img2_path]

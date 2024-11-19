from flask import Flask, request, render_template, send_file
from utils.movie_get import fetch_movie_details
from utils.image_generation import generate_images

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Collect form data
        movie_name = request.form.get("movie_name")
        venue = request.form.get("venue")
        time = request.form.get("time")

        try:
            # Fetch movie details
            movie_details = fetch_movie_details(movie_name)

            # Generate images
            image_paths = generate_images(movie_details, venue, time)

            # Pass image paths to the template
            return render_template("index.html", images=image_paths)
        except Exception as e:
            return render_template("index.html", error=str(e))

    # Default GET request
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

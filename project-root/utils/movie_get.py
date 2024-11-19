import requests
from config import IMDB_API_URL, IMDB_API_KEY

def fetch_movie_details(movie_name):
    params = {"t": movie_name, "apikey": IMDB_API_KEY}
    response = requests.get(IMDB_API_URL, params=params)
    data = response.json()

    if data.get("Response") == "True":
        movie_details = {
            "title": data["Title"],
            "year": data["Year"],
            "director": data["Director"],
            "description": data["Plot"],
            "poster_url": data["Poster"],
        }
        # Print the description to the terminal
        print(f"Description: {movie_details['description']}")
        return movie_details
    else:
        raise ValueError("Movie not found! Please try another title.")

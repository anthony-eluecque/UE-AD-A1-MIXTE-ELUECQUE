import requests

MOVIE_SERVICE_URL = "http://127.0.0.1:3200"

class MovieService:
    @staticmethod
    def get_movie_details(movie_id: str):
        url = f"{MOVIE_SERVICE_URL}/movies/{movie_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
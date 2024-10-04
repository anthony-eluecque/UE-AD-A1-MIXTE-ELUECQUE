import json
import uuid

MOVIES_DB_PATH = "{}/data/movies.json"
ACTORS_DB_PATH = "{}/data/actors.json"
class Json():
    
    @staticmethod
    def open(path : str, key : str):
        with open(path.format("."), "r") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def write(path: str,key: str, data):
        obj = {
            key : data
        }
        with open(path.format("."), "w") as wfile:
            json.dump(obj, wfile, indent=2)

def movie_with_id(_,info,_id):
    movies = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if movie['id'] == _id:
            return movie
            
def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    movies = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if movie['id'] == _id:
            movie['rating'] = _rate
            newmovie = movie
            newmovies = movies
    Json.write(MOVIES_DB_PATH, "movies", newmovies)
    return newmovie

def delete_movie_from_id(_, info, _id : str): 
    movies = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies :
        if movie['id'] == _id:
            movies.remove(movie)
            Json.write(MOVIES_DB_PATH, "movies", movies)
            return {
                "success": True
            }
    return {
        "success": False,
        "error": f"Movie with id : {_id} not existing"
    }

def create_movie(_, info, input):
    new_movie = {
        "id": str(uuid.uuid4()),
        "title": input["title"],
        "rating": input["rating"],
        "director": input["director"],
    }

    try:
        movies = Json.open(MOVIES_DB_PATH, "movies")

        for movie in movies:
            if movie["title"] == new_movie["title"]:
                return {
                    "success": False,
                    "error": "Movie existing"
                }
        movies.append(new_movie)
        Json.write(MOVIES_DB_PATH, "movies", movies)
        return {"success": True}
    except Exception as err:
        return {
            "success": False,
            "error": str(err),
        }

def movies_by_min_rate(_, info, _rate):
    return movies_by_field_with_conditions("rating", lambda rating: rating >= _rate)

def movies_by_director(_, info, _director):
    return movies_by_field_with_conditions("director", lambda director: director == _director)

def movie_with_title(_, info, _title):
    movies = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if movie["title"] == _title:
            return movie

def movies_by_field_with_conditions(key, condition_func):
    matching_movies = []
    movies = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if condition_func(movie[key]):
            matching_movies.append(movie)
    return matching_movies


def resolve_actors_in_movie(movie, info):
    actors = Json.open(ACTORS_DB_PATH, "actors")
    result = [actor for actor in actors if movie['id'] in actor['films']]
    return result
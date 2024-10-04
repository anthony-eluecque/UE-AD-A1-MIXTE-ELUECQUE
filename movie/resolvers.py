import json
from typing import TypedDict, Optional, List
import uuid

MOVIES_DB_PATH : str = "{}/data/movies.json"
ACTORS_DB_PATH : str = "{}/data/actors.json"

class MutationResponse(TypedDict):
    success : bool
    error :  Optional[str]

class Movie(TypedDict):
    id : str
    title : str
    director : str
    rating : float

class Actor(TypedDict):
    id : str
    firstname: str
    lastname : str
    birthyear : int 
    films : List[str]


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

def movie_with_id(_, info, _id : str) -> Movie | None:
    movies : List[Movie] = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if movie['id'] == _id:
            return movie
    return None
            
def update_movie_rate(_, info, _id : str, _rate : float) -> Movie:
    newmovies = {}
    newmovie : Movie
    movies : List[Movie] = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if movie['id'] == _id:
            movie['rating'] = _rate
            newmovie = movie
            newmovies = movies
    Json.write(MOVIES_DB_PATH, "movies", newmovies)
    return newmovie

def delete_movie_from_id(_, info, _id : str) -> MutationResponse: 
    movies : List[Movie] = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies :
        if movie['id'] == _id:
            movies.remove(movie)
            Json.write(MOVIES_DB_PATH, "movies", movies)
            return {
                "success": True,
                "error": None
            }
    return {
        "success": False,
        "error": f"Movie with id : {_id} not existing"
    }

def create_movie(_, info, input : Movie) -> MutationResponse:
    new_movie : Movie = {
        "id": str(uuid.uuid4()),
        "title": input["title"],
        "rating": input["rating"],
        "director": input["director"],
    }

    try:
        movies : List[Movie] = Json.open(MOVIES_DB_PATH, "movies")

        for movie in movies:
            if movie["title"] == new_movie["title"]:
                return {
                    "success": False,
                    "error": "Movie existing"
                }
        movies.append(new_movie)
        Json.write(MOVIES_DB_PATH, "movies", movies)
        return {
            "success": True, 
            "error": None
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err),
        }

def movies_by_min_rate(_, info, _rate : float) -> List[Movie]:
    return movies_by_field_with_conditions("rating", lambda rating: rating >= _rate)

def movies_by_director(_, info, _director : str) -> List[Movie]:
    return movies_by_field_with_conditions("director", lambda director: director == _director)

def movie_with_title(_, info, _title : str) -> Movie | None:
    movies : List[Movie] = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if movie["title"] == _title:
            return movie
    return None

def movies_by_field_with_conditions(key : str, condition_func) -> List[Movie]:
    matching_movies : List[Movie] = []
    movies : List[Movie] = Json.open(MOVIES_DB_PATH, "movies")
    for movie in movies:
        if condition_func(movie[key]):
            matching_movies.append(movie)
    return matching_movies


def resolve_actors_in_movie(movie : Movie, info) -> List[Actor]:
    actors : List[Actor] = Json.open(ACTORS_DB_PATH, "actors")
    result = [actor for actor in actors if movie['id'] in actor['films']]
    return result
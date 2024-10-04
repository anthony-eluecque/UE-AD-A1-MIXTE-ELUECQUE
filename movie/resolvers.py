import json
import uuid

def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie
            
def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile, indent=2)
    return newmovie

def delete_movie_from_id(_, info, _id : str) -> bool: 
    with open('{}/data/movies.json'.format("."), "r") as rfile: 
        movies = json.load(rfile)
        for movie in movies['movies'] :
            if movie['id'] == _id:
                movies['movies'].remove(movie)
                with open('{}/data/movies.json'.format("."), "w") as wfile:
                    json.dump(movies, wfile, indent=2)
                return True
    return False

def create_movie(_, info, input):
    movie = {
        "id": str(uuid.uuid4()),
        "title": input["title"],
        "rating": input["rating"],
        "director": input["director"],
    }
    with open('{}/data/movies.json'.format("."), "r") as rfile: 
        movies = json.load(rfile)
        movies["movies"].append(movie)
        with open('{}/data/movies.json'.format("."), "w") as wfile:
            json.dump(movies, wfile, indent=2)
    return movie

def movies_by_min_rate(_, info, _rate):
    return movies_by_field_with_conditions("rating", lambda rating: rating >= _rate)

def movies_by_director(_, info, _director):
    return movies_by_field_with_conditions("director", lambda director: director == _director)

def movie_with_title(_, info, _title):
    with open('./data/movies.json', "r") as rfile: 
        movies = json.load(rfile)
        for movie in movies["movies"]:
            if movie["title"] == _title:
                return movie

def movies_by_field_with_conditions(key, condition_func):
    matching_movies = []
    with open('./data/movies.json', "r") as rfile: 
        movies = json.load(rfile)
        for movie in movies["movies"]:
            if condition_func(movie[key]):
                matching_movies.append(movie)
    return matching_movies


def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        actors = json.load(file)
        result = [actor for actor in actors['actors'] if movie['id'] in actor['films']]
        return result
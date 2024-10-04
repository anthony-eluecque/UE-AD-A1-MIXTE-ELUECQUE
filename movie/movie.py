from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType, InputType
from flask import Flask, request, jsonify, make_response
import resolvers as r

PORT = 3001
HOST = '0.0.0.0'
app = Flask(__name__)

# todo create elements for Ariadne
mutation = MutationType()
type_defs = load_schema_from_path('movie.graphql')
query = QueryType()
movie = ObjectType('Movie')
actor = ObjectType('Actor')
movie_input = InputType('MovieInput')

movie.set_field('actors', r.resolve_actors_in_movie)

query.set_field('movie_with_id', r.movie_with_id)

mutation.set_field('update_movie_rate', r.update_movie_rate)
mutation.set_field('create_movie', r.create_movie)
mutation.set_field('delete_movie_from_id', r.delete_movie_from_id)

schema = make_executable_schema(type_defs, movie, query, mutation, actor, movie_input)

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

# graphql entry points
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()   
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code



if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType, InputType
from flask import Flask, request, jsonify, make_response
from api.resolvers import movie_resolvers as r
import os

schema_dirname, _filename = os.path.split(os.path.abspath(__file__))


base_types = load_schema_from_path(schema_dirname + '/base.graphql')
root_query = load_schema_from_path(schema_dirname + '/root.query.graphql')
root_mutation = load_schema_from_path(schema_dirname + '/root.mutation.graphql')
movies_types = load_schema_from_path(schema_dirname + '/movie.graphql')
actors_types = load_schema_from_path(schema_dirname + '/actor.graphql')

type_defs = [
    base_types,
    root_query,
    root_mutation,
    movies_types,
    actors_types
]

# # ============================================================= # 

mutation = MutationType()
query = QueryType()

query.set_field('movie_with_id', r.movie_with_id)
query.set_field('movies_by_min_rate', r.movies_by_min_rate)
query.set_field('movies_by_director', r.movies_by_director)
query.set_field('movie_with_title', r.movie_with_title)


mutation.set_field('update_movie_rate', r.update_movie_rate)
mutation.set_field('create_movie', r.create_movie)
mutation.set_field('delete_movie_from_id', r.delete_movie_from_id)

# # ============================================================= # 

movie = ObjectType('Movie')
actor = ObjectType('Actor')
mutation_result = ObjectType('MutationResult')
movie_input = InputType('MovieInput')

movie.set_field('actors', r.resolve_actors_in_movie)

schema = make_executable_schema(
    type_defs, 
    movie, 
    query, 
    mutation, 
    actor, 
    movie_input, 
    mutation_result
)
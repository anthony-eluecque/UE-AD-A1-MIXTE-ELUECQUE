from flask import jsonify, make_response, request, current_app
from .schemas import *
from .context import bp
from ariadne import graphql_sync

@bp.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)

@bp.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()   
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=current_app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
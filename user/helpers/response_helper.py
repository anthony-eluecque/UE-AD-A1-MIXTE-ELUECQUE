from flask import jsonify, make_response
from models import ERRORS

class ResponseHelper:

    @staticmethod
    def success(data=None, status_code=200):
        return make_response(jsonify(data if data is not None else {}), status_code)

    @staticmethod
    def error(error_key, status_code=None):
        error = ERRORS.get(error_key, ERRORS["INTERNAL_SERVER_ERROR"])
        status_code = status_code if status_code else error["code"]
        
        return make_response(jsonify({
            "error": error_key,
            "message": error["message"]
        }), status_code)
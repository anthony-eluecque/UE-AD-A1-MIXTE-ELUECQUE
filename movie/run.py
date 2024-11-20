from flask import Flask, request, jsonify, make_response
from api import create_app

PORT = 3001
HOST = '0.0.0.0'

if __name__ == "__main__":
    app = create_app()
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
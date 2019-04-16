from flask import Flask
from flask_restful import Resource, Api
from app.main.controller import {{cookiecutter.model_name}}_controller

app = Flask(__name__)
api = Api(app)

api.add_resource({{cookiecutter.model_name}}_controller, '/')

if __name__ == '__main__':
    app.run(debug=True)

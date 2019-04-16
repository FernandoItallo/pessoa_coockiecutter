from flask_restful import Resource


class {{cookiecutter.model_name}}Resource(Resource):
    def get(self):
        return {'hello': 'world'}

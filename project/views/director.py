from flask_restx import Resource, Namespace

from hw18_DV_hard.project.implemented import director_service
from lesson17_project_source.app import DirectorSchema

directors_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

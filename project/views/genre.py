from flask_restx import Resource, Namespace

from hw18_DV_hard.project.dao.model.genre import GenreSchema
from hw18_DV_hard.project.implemented import genre_service

genres_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

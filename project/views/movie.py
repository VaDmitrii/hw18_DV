from flask import request
from flask_restx import Resource, Namespace

from hw18_DV_hard.project.dao.model.movie import MovieSchema
from hw18_DV_hard.project.implemented import movie_service

movies_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        req_obj = request.args
        movies = movie_service.get_all(req_obj)
        return movies_schema.dump(movies), 200

    def post(self):
        req_obj = request.json
        movie_service.post(req_obj)
        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_obj = request.json
        req_obj['mid'] = mid

        movie_service.update(req_obj)

        return '', 204

    def patch(self, mid):
        req_obj = request.json
        req_obj["mid"] = mid

        movie_service.update_partial(req_obj)

        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204

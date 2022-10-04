from hw18_DV_hard.project.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self, data):
        return self.movie_dao.get_all(data)

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def post(self, data):
        return self.movie_dao.post(data)

    def update(self, data):
        mid = data.get("mid")
        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")

        return self.movie_dao.update(movie)

    def update_partial(self, data):
        mid = data.get("mid")
        movie = self.get_one(mid)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")

        return self.movie_dao.update(movie)

    def delete(self, mid):
        return self.movie_dao.delete(mid)

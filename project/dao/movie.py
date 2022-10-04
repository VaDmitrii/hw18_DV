from hw18_DV_hard.project.dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self, data):
        director_id = data.get("director_id")
        genre_id = data.get("genre_id")
        year = data.get("year")
        movies_query = self.session.query(Movie)

        if director_id:
            movies_query = movies_query.filter(Movie.director_id == director_id)
        if genre_id:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)
        if year:
            movies_query = movies_query.filter(Movie.year == year)

        return movies_query.all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def post(self, data):
        new_movie = Movie(**data)

        self.session.add(new_movie)
        self.session.commit()

        return new_movie

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()



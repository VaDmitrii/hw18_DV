from marshmallow import Schema, fields

from hw18_DV_hard.project.dao.model.director import Director
from hw18_DV_hard.project.dao.model.genre import Genre
from hw18_DV_hard.project.setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship(Genre)
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship(Director)


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()

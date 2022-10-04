from flask_restx import Namespace
from marshmallow import Schema, fields

from hw18_DV_hard.project.setup_db import db

ns_genres = Namespace('genres')


class Genre(db.Model):
    __tablename__ = 'genre'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

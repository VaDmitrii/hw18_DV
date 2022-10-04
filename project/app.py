from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie import movies_ns
from views.director import directors_ns
from views.genre import genres_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    return app


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


#    create_data(app, db)


# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)


app = create_app(Config())
register_extensions(app)

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

from flask import Flask
from core.database import init_db
import logging


def create_app():

    createapp = Flask(__name__)

    # Flask Config
    createapp.config.from_object('config')

    # sqlalchemy log setting
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy.orm.unitofwork').setLevel(logging.DEBUG)

    # database.py
    init_db(createapp)

    return createapp


app = create_app()

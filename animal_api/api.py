from constants import PROJECT_ROOT, ANIMAL_FACTS_DATABASE
from resources.facts_resources import FactsResource, FACTS_ENDPOINT
from database import db
from flask import Flask
from flask_restful import Api
import logging
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def create_app(db_location):
    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-RESTful API,
    and Flask-SQLAlchemy connection

    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """
    # This configures our logging, writing all logs to the file "animal_api.log"
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("animal_api.log"), logging.StreamHandler()],
    )

    current_app = Flask(__name__)
    current_app.config["SQLALCHEMY_DATABASE_URI"] = db_location
    db.init_app(current_app)

    api = Api(current_app)
    api.add_resource(FactsResource, FACTS_ENDPOINT, f"{FACTS_ENDPOINT}/<id>")
    return current_app


if __name__ == "__main__":
    app = create_app(f"sqlite:////{PROJECT_ROOT}/{ANIMAL_FACTS_DATABASE}")
    app.run(debug=True, host="localhost", port=6789)

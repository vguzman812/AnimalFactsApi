import logging

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound

from animal_api.database import db
from animal_api.models.fact import Fact
from animal_api.schemas.fact_schema import FactSchema

FACTS_ENDPOINT = "/api/facts"
logger = logging.getLogger(__name__)


class FactsResource(Resource):
    def get(self, id=None):
        """
        FactsResource GET method. Retrieves all facts found in the Facts database,
        unless the id path parameter is provided. If this id
        is provided then the fact with the associated fact_id is retrieved.

        :param id: Fact ID to retrieve, this path parameter is optional
        :return: Fact, 200 HTTP status code
        """
        if not id:
            name = request.args.get("animal_name")
            logger.info(
                f"Retrieving all facts, optionally filtered by name={name}"
            )

            return self._get_all_facts(name), 200

        logger.info(f"Retrieving fact by id {id}")

        try:
            return self._get_fact_by_id(id), 200
        except NoResultFound:
            abort(404, message="Fact id not found")

    def _get_fact_by_id(self, fact_id):
        fact = Fact.query.filter_by(fact_id=fact_id).first()
        fact_json = FactSchema().dump(fact)

        if not fact_json:
            raise NoResultFound()

        logger.info(f"Fact retrieved from database {fact_json}")
        return fact_json

    def _get_all_facts(self, name):
        if name:
            facts = Fact.query.filter_by(animal_name=name).all()
        else:
            facts = Fact.query.all()

        facts_json = [FactSchema().dump(fact) for fact in facts]

        logger.info("Facts successfully retrieved.")
        return facts_json

    def post(self):
        """
        FactsResource POST method. Adds a new Fact to the database.

        :return: Fact.fact_id, 201 HTTP status code.
        """
        fact = FactSchema().load(request.get_json())

        try:
            db.session.add(fact)
            db.session.commit()
        except IntegrityError as e:
            logger.warning(
                f"Integrity Error, this fact is already in the database. Error: {e}"
            )

            abort(500, message="Unexpected Error!")
        else:
            return fact.fact_id, 201

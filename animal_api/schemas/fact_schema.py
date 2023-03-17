from marshmallow import Schema, fields, post_load
from models.fact import Fact


class FactSchema(Schema):
    """
    Fact Marshmallow Schema
    Marshmallow schema used for loading/dumping Facts
    """

    fact_id = fields.Integer()
    animal_name = fields.String(allow_none=False)
    source = fields.String(allow_none=False)
    text = fields.String(allow_none=False)
    media_link = fields.String()
    wikipedia_link = fields.String(allow_none=False)

    @post_load
    def make_fact(self, data, **kwargs):
        return Fact(**data)

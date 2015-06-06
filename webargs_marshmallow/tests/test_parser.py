from flask import Flask
from marshmallow import Schema, fields
import pytest
from webargs.flaskparser import FlaskParser

from ..parser import SchemaParserMixin


class FlaskSchemaParser(SchemaParserMixin, FlaskParser):
    pass


flask_schema_parser = FlaskSchemaParser()
use_args = flask_schema_parser.use_args


class HelloSchema(Schema):
    name = fields.Str()


class TestAppConfig(object):
    TESTING = True
    DEBUG = True


@pytest.fixture
def test_app():
    app = Flask(__name__)
    app.config.from_object(TestAppConfig)

    @app.route('/')
    @use_args(HelloSchema)
    def index(hello):
        return 'Hello ' + hello['name']

    return app


def test_parsing_get_args(test_app):
    test_client = test_app.test_client()
    res = test_client.get('/?name=world')
    assert res.data.decode("utf-8") == "Hello world"

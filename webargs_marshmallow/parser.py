"""
"""

import functools

from webargs import Arg


class SchemaParserMixin(object):
    """
    """

    def parse(self, schema_cls, req, locations=None, validate=None, force_all=False):
        # TODO: how to handle collections?
        schema = schema_cls()

        argmap = dict(
            (name, _to_arg(field))
            for name, field in schema.fields.items())

        print argmap

        parsed = (
            super(SchemaParserMixin, self)
            .parse(argmap, req, locations, validate, force_all))

        print parsed

        result = schema.load(parsed)

        print result.data

        # TODO: handle error
        return result.data


def _to_arg(field):
    """
    """
    # TODO: handle nested fields
    # TODO: add mapping of field types for type coercion
    return Arg()

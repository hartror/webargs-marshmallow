# webargs-marshmallow

webargs-marshmallow provides a webargs parser that understands marshmallow
schemas.

```
from flask import Flask
from webargs import Arg
from webargs.flaskparser import parser
import webargs_marshmallow

schema_parser = webargs_marshmallow.Parser(parser)
use_schema_args = schema_parser.use_schema_args

app = Flask(__name__)

class HelloSchema(Schema):
    name = fields.Str()

@app.route('/')
@use_schema_args(HelloSchema)
def index(hello):
    return 'Hello ' + hello['name']

if __name__ == '__main__':
    app.run()

# curl http://localhost:5000/\?name\='World'
# Hello World
```

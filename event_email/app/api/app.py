import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from marshmallow import ValidationError
from simplejson import JSONDecoder, JSONEncoder
from webargs.flaskparser import parser
from werkzeug.exceptions import HTTPException

from event_email.app.api.apis import email_api, event_api
from event_email.app.api.common.exceptions import FailResponse

app = Flask(__name__)
CORS(app)
app.json_decoder = JSONDecoder  # type: ignore
app.json_encoder = JSONEncoder  # type: ignore

app.register_blueprint(email_api.blp, url_prefix="/api/email")
app.register_blueprint(event_api.blp, url_prefix="/api/event")

if os.getenv('APP_ENV') in ['local']:
    from apispec import APISpec
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec, ResourceMeta
    from types import FunctionType

    marshmallow_plugin = MarshmallowPlugin()

    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='Balance',
            version='v1',
            plugins=[marshmallow_plugin],
            openapi_version='2.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })

    docs = FlaskApiSpec(app, document_options=False)
    for (fpath, view_function) in app.view_functions.items():
        blueprint_name = fpath.split('.')[0]
        if fpath != 'static' and (isinstance(view_function, FunctionType) or isinstance(view_function, ResourceMeta)):
            docs.register(view_function, blueprint=blueprint_name)


@app.errorhandler(Exception)
def handle_exception(error):
    err_msg = 'Error during accessing {url}'.format(url=request.path)
    try:
        spec = request.get_json()
    except:
        spec = None
    if isinstance(error, HTTPException):
        response = jsonify({'message': error.description})
        response.status_code = error.code
        err_msg += ' because {desc}'.format(desc=error.description)
    elif isinstance(error, FailResponse):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        err_msg += ' with request spec: {spec}'.format(spec=spec)
    elif isinstance(error, ValidationError):
        response = jsonify({'json': error.messages, 'message': 'Validation error', 'errorCode': 'API_VALIDATION_ERROR'})
        response.status_code = 422
        err_msg += ' with request spec: {spec}'.format(spec=spec)
    else:
        response = jsonify({'message': 'Unexpected error, please contact system administrator or try again later.'})
        response.status_code = 500
        err_msg += ' with request spec: {spec}'.format(spec=spec)
        return response
    return response


@parser.error_handler
def handle_error(error, *_args, **_kwargs):
    raise FailResponse(message="Validation error", status_code=422,
                       payload=error.messages['json'] if 'json' in error.messages else error.messages['form'],
                       error_code='API_VALIDATION_ERROR')

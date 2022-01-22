from flask_restx import Api

from src import __version__, app
from src.api.v1.ca import ns as ca_v1
from src.api.v1.commom_models import api_models_namespace

api = Api(
    app,
    version=__version__.version,
    title="OwnCA REST API",
    description="OwnCA REST API",
)

api.add_namespace(api_models_namespace)
api.add_namespace(ca_v1, path="/api/v1/ca")

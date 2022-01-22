from flask_restx import Namespace, fields

api_models_namespace = Namespace("Models")

error_model = api_models_namespace.model(
    "error_model",
    {
        "message": fields.String(
            description="error message",
            example="Permission Denied on OwnCA storage.",
        ),
    },
)

oids = api_models_namespace.model(
    "oids",
    {
        "country_name": fields.String(
            description="Country Name",
            example="NL",
            max=2,
        ),
        "locality_name": fields.String(
            description="Locality referece",
            example="Veldhoven",
        ),
        "state_or_province": fields.String(
            description="State or Provice",
            example="Noord-Brabant",
        ),
        "street_address": fields.String(
            description="Street Name",
            example="Straat",
        ),
        "organization_name": fields.String(
            description="Organization name",
            example="Example Org",
        ),
        "organization_unit_name": fields.String(
            description="Organization Unit Name",
            example="Unit Example",
        ),
        "email_address": fields.String(
            description="State or Provice",
            example="certificates@example.com",
        ),
    },
)

from flask import jsonify
from flask_restx import Namespace, Resource, fields

from src.api.v1.commom_models import error_model, oids

ns = Namespace("/ca", description="Certificate Authorities")


@ns.route("")
class CertificateAuthority(Resource):

    ca_list_data = ns.model(
        "certificate_authorities",
        {
            "certificate_authorities": fields.List(
                fields.String(
                    description="Certificate Authority common name",
                    example="ca.example.com",
                ),
                description="Certificate Authorities",
                example=["ca.example.com", "internal.example.com"],
                required=True,
            )
        },
    )
    certificate_authorities_response = ns.model(
        "certificate_authorities_data",
        {
            "data": fields.Nested(ca_list_data),
            "error": fields.Nested(error_model),
        },
    )

    @ns.response(200, "OK", certificate_authorities_response)
    def get(self):
        """List all Certificate Authorities"""


    post_certificate_authority = ns.model(
        "post_certificate_authority",
        {
            "common_name": fields.String(
                description="Certificate Authority Common Name",
                required=True,
                example="example.com",
            ),
            "dns_names": fields.List(
                fields.String(
                    description="Aditional names",
                    required=True,
                    example="www.example.com",
                ),
                description="List of additional names",
                example=["www.example.com", "example.com", "example.nl"],
            ),
            "intermediate": fields.Boolean(
                description="Is it a intermediate Certificate Authority?",
                required=False,
                default=False,
                example=False,
            ),
            "oids": fields.Nested(oids),
            "public_exponent": fields.Integer(
                description="Public Exponent for the Key",
                default=65537,
                example=65537,
            ),
            "key_size": fields.Integer(
                description="Key size",
                default=2048,
                example=2048,
            ),
        },
    )

    @ns.doc(body=post_certificate_authority, validate=True)
    def post(self):
        """Add new Certificate Authorities"""


@ns.route("/<ca_common_name>")
@ns.doc(params={"ca_common_name": "Certificate Authority Common Name"})
class CertificateAuthorityManagement(Resource):

    ca_data = ns.model(
        "ca_data",
        {
            "common_name": fields.String(
                description="Certificate Authority common name",
                example="ca.example.com",
                required=True,
            ),
            "certificate": fields.String(
                description="Certificate",
                example=(
                    "-----BEGIN CERTIFICATE-----"
                    + "RdXfXcn7qTeMMZE531OoEYgmkUEvlntuRPpSZU6g/+PoxS6P5(...)"
                    "-----END CERTIFICATE-----"
                ),
            ),
            "intermediate_ca": fields.Boolean(
                description="Is this a intermediate CA?",
                example=False,
                required=True,
            ),
            "hash_name": fields.String(
                description="Hash name",
                example="4f135327",
            ),
            "private_key": fields.String(
                description="Private key",
                example=(
                    "-----BEGIN PRIVATE KEY-----"
                    + "+v/bnEp2n/QWTbu10Tzk2glhsj2GQxU9E5uZaZrAEdn6nRhV3(...)"
                    "-----END PRIVATE KEY-----"
                ),
                required=True,
            ),
            "public_key": fields.String(
                description="Public key",
                example="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC(...)",
                required=True,
            ),
            "crl": fields.String(
                description="Certificate Revocation List",
                example=(
                    "-----BEGIN X509 CRL-----"
                    "A5MTExODM5WhcNMjIwMTEwMTExODM5WjAkMCICEQCLAOWnqE9LMp(...)"
                    "-----END X509 CRL-----"
                ),
            ),
            "csr": fields.String(
                description="Certificate Signing Request",
                example=(
                    "-----BEGIN CERTIFICATE REQUEST-----"
                    "q0fDSFPwUTAHjLUU4Nih635GsfRHMP96r8U25a1Z7hqHWBcsMOGZ(...)"
                    "-----END CERTIFICATE REQUEST-----"
                ),
            ),
            "issued_certificates": fields.List(
                fields.String(
                    description="Certificate Common Name",
                    example="www.example.com",
                ),
                description="List of issued certificates",
                example=["intranet.example.com", "mail.example.net"],
            ),
        },
    )
    get_common_name_response = ns.model(
        "get_common_name_response",
        {
            "data": fields.Nested(ca_data),
            "error": fields.Nested(error_model),
        },
    )

    @ns.response(200, "OK", get_common_name_response)
    def get(self, ca_common_name):
        """Get information of specific Certificate Authority"""

    certificate_intermediate_ca = ns.model(
        "certificate_intermediate_ca",
        {
            "certificate": fields.String(
                description="Certificate",
                example=(
                    "-----BEGIN CERTIFICATE-----"
                    "R8dXfXcn7qTeMMZE531OoEYgmkUEvlntuRPpSZU6gIy/+PoxS6P5(...)"
                    "-----END CERTIFICATE-----"
                ),
                required=True,
            ),
        },
    )

    @ns.doc(body=certificate_intermediate_ca, validate=True)
    @ns.response(200, "OK", get_common_name_response)
    def put(self, ca_common_name):
        """Add Signed Certificate for Intermediate Certificate Authority"""


@ns.route("/<ca_common_name>/certificates")
class CertificateAuthorityCertificates(Resource):

    ca_certs_data = ns.model(
        "ca_certs_data",
        {
            "certificates": fields.List(
                fields.String(
                    description="Certificate Common Name",
                    example="www.example.com",
                ),
                description="List of issued certificates",
                required=True,
            )
        },
    )
    get_certificates_response = ns.model(
        "get_certificates_response",
        {
            "data": fields.Nested(ca_certs_data),
            "error": fields.Nested(error_model),
        },
    )

    @ns.response(200, "OK", get_certificates_response)
    def get(self, ca_common_name):
        """Get Certificate Authority Certificates"""

    ca_certificate = ns.model(
        "post_ca_certificate",
        {
            "common_name": fields.String(
                description="Certificate common name",
                example="www.example.com",
                required=True,
            ),
            "maximum_days": fields.Integer(
                description="Maximum days to expire",
                example=365,
                max=825,
                default=825,
            ),
            "dns_names": fields.List(
                fields.String(
                    description="Aditional names",
                    required=True,
                    example="www.example.com",
                ),
                description="List of additional names",
                example=["www.example.com", "example.com", "example.nl"],
            ),
            "oids": fields.Nested(oids),
            "public_exponent": fields.Integer(
                description="Public Exponent for the Key",
                default=65537,
                example=65537,
            ),
            "key_size": fields.Integer(
                description="Key size",
                default=2048,
                example=2048,
            ),
        },
    )
    post_ca_certifica_response = ns.model(
        "post_ca_certificate_response",
        {
            "data": fields.Nested(ca_certificate),
            "error": fields.Nested(error_model),
        },
    )

    @ns.response(200, "OK", post_ca_certifica_response)
    @ns.doc(body=ca_certificate, validate=True)
    def post(self, ca_common_name):
        """Issue new certificate"""


@ns.route("/<ca_common_name>/certificates/<certificate_common_name>")
@ns.doc(
    params={
        "ca_common_name": "Certificate Authority Common Name",
        "certificate_common_name": "Certificate Common Name",
    }
)
class CertificateAuthorityCertificateManagement(Resource):

    certificate_data = ns.model(
        "certificate_data",
        {
            "common_name": fields.String(
                description="Certificate common name",
                example="www.example.com",
                required=True,
            ),
            "certificate": fields.String(
                description="Certificate",
                example=(
                    "-----BEGIN CERTIFICATE-----"
                    + "R8dXfXcn7qTeMMZE531OoEYgmkUEvtuRPpSZU6gIy/+PoxS6P5(...)"
                    "-----END CERTIFICATE-----"
                ),
            ),
            "private_key": fields.String(
                description="Private key",
                example=(
                    "-----BEGIN PRIVATE KEY-----"
                    + "+v/bnEp2n/QWTbu10Tzk2glhsj2GQxE5uZaZB1lrAEdn6nRhV3(...)"
                    "-----END PRIVATE KEY-----"
                ),
                required=True,
            ),
            "public_key": fields.String(
                description="Public key",
                example="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC(...)",
                required=True,
            ),
            "csr": fields.String(
                description="Certificate Signing Request",
                example=(
                    "-----BEGIN CERTIFICATE REQUEST-----"
                    "q0fDSFPwUTAHjLUU4Nih635GsfRHMP96r8U25a1Z7hqHWBcsMOGZ(...)"
                    "-----END CERTIFICATE REQUEST-----"
                ),
            ),
        },
    )
    get_certificate_response = ns.model(
        "get_certificate_response",
        {
            "data": fields.Nested(certificate_data),
            "error": fields.Nested(error_model),
        },
    )

    @ns.response(200, "OK", get_certificate_response)
    def get(self, ca_common_name, certificate_commom_name):
        """Get Certificate Authority of specific certificate information"""

    def delete(self, ca_common_name, certificate_commom_name):
        """Revoke Certificate Authority of specific certificate"""

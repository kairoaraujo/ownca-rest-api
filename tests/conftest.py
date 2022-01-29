from dataclasses import dataclass

import pytest
from werkzeug.test import TestResponse
from app import ownca_api_app


@dataclass
class RequestData:
    method: str
    endpoint: str
    payload: dict


@pytest.fixture
def api_request():
    def _api_request(request_data: RequestData) -> TestResponse:

        with ownca_api_app.test_client() as api_client:
            with ownca_api_app.app_context():
                if request_data.method.lower() == "get":
                    response = api_client.get(
                        request_data.endpoint, json=request_data.payload
                    )

                elif request_data.method.lower() == "post":
                    response = api_client.post(
                        request_data.endpoint, json=request_data.payload
                    )

                elif request_data.method.lower() == "put":
                    response = api_client.put(
                        request_data.endpoint, json=request_data.payload
                    )

                elif request_data.method.lower() == "delete":
                    response = api_client.delete(
                        request_data.endpoint, json=request_data.payload
                    )

                else:
                    raise ValueError("Invalid HTTP methord")

                return response

    return _api_request

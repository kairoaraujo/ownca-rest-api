"""Certificate Authority feature tests."""
import json

from pytest_bdd import given, parsers, scenarios, then, when

from tests.conftest import RequestData, api_request

scenarios(
    "../features/ca.feature",
)


@given("I am a JSON API User")
def i_am_a_json_api_user(api_request):
    """I am a JSON API User."""
    response = api_request(RequestData("get", "/", {}))
    assert response.status_code == 200


@when('I request GET "/api/v1/ca"', target_fixture="request_data")
def i_request_get_apiv1ca():
    """I request GET "/api/v1/ca"."""
    request_data = RequestData("get", "/api/v1/ca", {})
    return request_data


@then(
    parsers.cfparse('I should get a status code of 200 with json {response}')
)
def i_should_get_a_status_code_of_200_with_json_response(
    api_request, request_data, response
):
    """I should get a status code of 200 with json <response>."""
    test_response = api_request(request_data)
    assert test_response.status_code == 200
    assert test_response.json == json.loads(response)


@when(
    parsers.cfparse(
        'I request POST "/api/v1/ca" using {payload} as JSON body'
    ),
    target_fixture="request_data",
)
def i_request_post_v1apica_using_payload_as_json_body(payload):
    """I request POST "/api/v1/ca" using {payload} as JSON body."""
    payload_body = json.loads(payload)
    request_data = RequestData("post", "/api/v1/ca", payload_body)
    return request_data


@then("I should get a status code of 201")
def i_should_get_a_status_code_of_201(api_request, request_data):
    """I should get a status code of 201."""
    test_response = api_request(request_data)
    assert test_response.status_code == 201

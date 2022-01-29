Feature: Certificate Authority

    As an API User, I want to be able to manage the Certificate Authorities.

    Scenario Outline: Get all Certificate Authority WITHOUT having any Certificate Authorities
        Given I am a JSON API User
        When I request GET "/api/v1/ca"
        Then I should get a status code of 200 with json <response>
        Examples:
        |response                                               |
        |{"data": {"certificate_authorities": []},"error": null}|

    Scenario Outline: Add a Certificate Authority to the OwnCA REST API Service
        Given I am a JSON API User
        When I request POST "/api/v1/ca" using <payload> as JSON body
        Then I should get a status code of 201
        Examples: Payloads
        |payload                                                             |
        |{"common_name": "example.com"}                                      |
        |{"common_name": "nl.example.nl", "dns_names": ["www.nl.example.nl"]}|

    Scenario Outline: Get all Certificate Authority having Certificate Authorities
        Given I am a JSON API User
        When I request GET "/api/v1/ca"
        Then I should get a status code of 200 with json <response>
        Examples:
        |response                                                            |
        |{"data": {"certificate_authorities": ["example.com", "nl.example.nl"]},"error": null}|


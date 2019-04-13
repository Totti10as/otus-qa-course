"""
https://dog.ceo/dog-api/
"""
import pytest
import json


@pytest.mark.positive
def test_status_200(get_endpoints):
    """ Test status code """
    assert get_endpoints.status_code == 200


@pytest.mark.positive
def test_response_headers(get_endpoints):
    assert get_endpoints.headers['Content-type'] == 'application/json'


@pytest.mark.positive
def test_response_json(get_endpoint):
    assert get_endpoint.json()['status'] == 'success'


@pytest.mark.negative
def test_status_404(get_bad_endpoint):
    assert get_bad_endpoint.status_code == 404


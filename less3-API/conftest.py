"""Conftest"""

import pytest
import requests

API_ENDPOINTS = [
    "https://dog.ceo/api/breed/hound/afghan/images/random/3",
    "https://dog.ceo/api/breeds/image/random",
    "https://dog.ceo/api/breeds/list/all"]
ENDPOINTS_PARAM = '/bad-param'

@pytest.fixture(params=API_ENDPOINTS)
def get_endpoints():
    for url in API_ENDPOINTS:
        url = requests.get(url)
        return url

@pytest.fixture()
def get_endpoint():
    url = API_ENDPOINTS[0]
    url = requests.get(url)
    return url


@pytest.fixture(params=API_ENDPOINTS)
def get_bad_endpoint():
    for url in API_ENDPOINTS:
        url = requests.get(url + ENDPOINTS_PARAM)
        return url

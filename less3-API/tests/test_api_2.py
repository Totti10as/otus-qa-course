"""
https://dog.ceo/dog-api/
"""
import pytest
import requests

api_endpoints = ["https://api.cdnjs.com/libraries", "https://api.openbrewerydb.org/breweries", "https://dog.ceo/api/breeds/list/all"]
my_links = [requests.get(link) for link in api_endpoints]

@pytest.mark.parametrize("x", my_links)
def test(x):
    assert x.status_code == 200
    print(x)



# @pytest.fixture()
# def response():
#     my_links = [requests.get(link) for link in api_endpoints]
#     return my_links
#
#
# @pytest.mark.usefixtures("response")
# def test_status(response):
#     assert response.status_code == 200








# @pytest.fixture()
# def response():
#     api_endpoints = ["https://api.cdnjs.com/libraries", "https://api.openbrewerydb.org/breweries",
#                      "https://dog.ceo/api/breeds/list/all"]
#     my_links = [requests.get(link) for link in api_endpoints]
#     return my_links
#
#
# @pytest.mark.usefixtures("response")
# def test_endpoints_content_type():
#     assert my_links == 200




# @pytest.fixture()
# def verify_status():
#     my_links = [requests.get(link) for link in api_endpoints]
#     return my_links


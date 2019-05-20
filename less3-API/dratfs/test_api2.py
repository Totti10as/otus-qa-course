import pytest
import requests

urls = ["https://api.cdnjs.com/libraries", "https://api.openbrewerydb.org/breweries", "https://dog.ceo/api/breeds/list/all"]
#headers = [{"Content-type": "application/json"}, {"Content-type": "text/html"}, {}]
#pairs = [url for url in urls]


@pytest.fixture(urls)
def response(request):
    return requests.get(urls)


@pytest.mark.usefixtures("response")
def test_urls(response):
    assert response.status_code == 200
# my_links = [requests.get(link) for link in api_endpoints]

# api_endpoints = ["https://dog.ceo/api/breed/hound/afghan/images/random/3",
#                  "https://dog.ceo/api/breeds/image/random", "https://dog.ceo/api/breeds/list/all"]
#
# return api_endpoints




# ------------------- 2 example - work as expected  --------------------------------------------


# api_endpoints = ["https://dog.ceo/api/breed/hound/afghan/images/random/3", "https://dog.ceo/api/breeds/image/random",
#                  "https://dog.ceo/api/breeds/list/all"]
# my_links = [requests.get(link) for link in api_endpoints]
#
#
# @pytest.mark.parametrize("status_ok", my_links)
# def test_status(status_ok):
#     #print('\n-------- 2 example -------')
#     assert status_ok.status_code == 200
#     #print("2 example - work as expected")
#


#@pytest.mark.parametrize("status_ok", endpoint_status)

#@pytest.mark.usefixtures("get_endpoints")
#@pytest.mark.parametrize("endpoint", get_endpoints)

#@pytest.mark.usefixtures("get_endpoints")


# def valid_endpoints(get_endpoints):

#endpoint_status = [requests.get(link) for link in get_endpoints]
#     return endpoint_status




   #endpoint_status = [requests.get(link) for link in get_endpoints]


   # print(type(endpoint_status))

    #endpoint_status = [requests.get(link) for link in get_endpoints]
   # print(status_ok)
    #assert endpoint_status.status_code == 200
    #print(status_ok)

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

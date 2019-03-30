"""Conftest"""

import pytest


@pytest.fixture(scope="session", autouse=True)
def start_of_session(request):
    print('\n *** Start of run: The session is began *** ')

    def enf_of_session():
        print('\n *** End of run: The session is ended *** ')
    request.addfinalizer(enf_of_session)


@pytest.fixture()
def setup():
    print("Running conftest method setUP")
    print("-"*30)
    yield
    print("\nRunning conftest method tearDown")
    print("-" * 30)


@pytest.fixture(scope="module")
def onetimesetup():
    print("\nRunning conftest one time setUP")
    print("-" * 30)
    yield
    print("Running conftest one time tearDown")
    print("-" * 30)

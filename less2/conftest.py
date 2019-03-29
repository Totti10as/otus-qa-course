import pytest

@pytest.fixture()
def setup():
    print("\n Running conftest method setUP")
    yield
    print("\n Running conftest method tearDown")


@pytest.fixture(scope="module")
def onetimesetup():
    print("\n Running conftest one time setUP")
    yield
    print("\n Running conftest one time tearDown")
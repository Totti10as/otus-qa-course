""" Testing login page """

import pytest


@pytest.mark.positive
@pytest.mark.usefixtures("login_valid")
def test_valid_login(driver):
    """
    Run positive test
    with the following commandline:
    python -m pytest -m positive -s -v test_login.py --browser chrome
    """
    assert driver.title == 'Dashboard'


@pytest.mark.negative
def test_invalid_login(driver, login_invalid):
    """
    Run negative test
    with the following commandline:
    python -m pytest -m negative -s -v test_login.py --browser chrome
    """
    assert login_invalid == 'No match for Username and/or Password.\n×'

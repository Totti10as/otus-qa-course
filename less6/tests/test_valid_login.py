""" Testing login page - positive tests """

import pytest


@pytest.mark.usefixtures("login_valid")
def test_valid_login(driver):
    """
    Run positive test
    with the following commandline:
    python -m pytest -m positive -s -v test_valid_login.py --browser chrome
    """
    assert driver.title == 'Dashboard'




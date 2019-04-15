""" Testing login page - negative tests """


def test_invalid_login(driver, login_invalid):
    """
    Run negative test
    with the following commandline:
    python -m pytest -m negative -s -v test_valid_login.py --browser chrome
    """
    assert login_invalid == 'No match for Username and/or Password.\n×'

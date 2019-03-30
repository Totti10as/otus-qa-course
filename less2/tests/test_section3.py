''' Run demo test scenarions '''

import pytest
from less2.data.numbers import Math
from less2.data.strings import uplowcase
from less2.data.strings import join_strings
from less2.data.carslist import cars_list

# ---------------------------------------------------------------------------

@pytest.mark.run(order=1)
def test_sumnums(onetimesetup, setup):
    """
    Verify function that add two numbers
    """
    print('Verifying function that add two numbers')
    result = Math(10, 20)
    assert result.sum_nums() == 30, "The Add Method function is broken"

# ---------------------------------------------------------------------------

@pytest.mark.run(order=2)
def test_subnums(onetimesetup, setup):
    """
    Verify function that subtract two numbers
    """
    print('Verifying function that subtract two numbers')
    result = Math(20, 10)
    assert result.sub_nums() == 10

# ---------------------------------------------------------------------------

# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order=3)
def test_joinstrings(onetimesetup, setup):
    """
    Verify join strings function

    """
    print('Verifying function that join strings')
    assert join_strings('Automation', 'Course') == 'Automation Course'

# ---------------------------------------------------------------------------


@pytest.mark.run(order=4)
def test_uplowcase(onetimesetup, setup):
    """
       Verify upper and lower case in string

    """
    print('Verifying function that count upper and lower case in string')
    res1, res2 = uplowcase("Automation String")
    assert res1 == 2 and res2 == 14

# ---------------------------------------------------------------------------


# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order=5)
def test_listlength(onetimesetup, setup):
    """
    Verify length function

    """
    print('Verifying length function')
    my_list = [1, 2, 3, 's', 5, 6, 7, 8]
    assert cars_list(my_list) == 8

# ---------------------------------------------------------------------------


@pytest.mark.run(order=6)
def test_wordinsets(onetimesetup, setup):
    """
  Verify fruit string in sets
  """
    print('Verifying function of Set')
    fruits = {"apple", "banana", "mango", "strawberry"}
    result = "mango" in fruits
    assert result

# ---------------------------------------------------------------------------


@pytest.mark.run(order=7)
def test_wordintuple(onetimesetup, setup):
    """
      Verify fruit string in Tuple
      """
    print('Verifying function of Tuple')
    fruits = ("apple", "banana", "mango", "strawberry")
    assert fruits[2] == 'mango'
# ---------------------------------------------------------------------------


@pytest.mark.usefixtures("onetimesetup", "setup")
@pytest.mark.run(order=8)
def test_dictionary():
    """
      Verify car model value in dictionary
    """
    print('Verifying function of Dictionary')
    cars = {'bmw': {'model': 'x3', 'year': 2019}, 'mazda': {'model': 'cx5', 'year': 2019}}
    bmw_model = cars['bmw']['model']
    assert bmw_model == 'x3'

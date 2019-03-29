''' Run demo test scenarions '''

import pytest
from less2.data.numbers import Math
from less2.data.strings import join_strings
from less2.data.carslist import cars_list



@pytest.mark.run(order=1)
def test_sumnum():
    """
    # Verify function that sums two numbers
    """
    result = Math.sum_num(10, 20)
    assert result == 30

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order=2)
def test_joinstrings():
    """
    # Verify join strings function

    """
    assert join_strings('Automation', 'Course') == 'Automation Course'

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.run(order=3)
def test_listlength():
    """
    # Verify length function

    """
    my_list = [1, 2, 3, 's', 5, 6, 7, 8]
    assert cars_list(my_list) == 8

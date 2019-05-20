import pytest

@pytest.mark.parametrize("y", [2, 3])
@pytest.mark.parametrize("x", [0, 1])
def test_foo(x, y):
    print(x, y)

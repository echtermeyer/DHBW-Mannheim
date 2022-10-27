import pytest
from hypothesis import strategies, given


def my_sum(a, b):
    return a + b


# #### UNITTESTS ######


# postiver Test
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (10, 20, 30),
        (1.70, 1.30, 3.0),
    ],
)
def test_my_sum(a, b, expected):
    assert my_sum(a, b) == expected


# negativer Test, macht so wenig Sinn...
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 4),
        (10, 20, 1020),
    ],
)
def test_my_sum(a, b, expected):
    with pytest.raises(AssertionError):
        assert my_sum(a, b) == expected


# ############ Property Based Testing ############


# postiver Test
@given(
    a=strategies.one_of(strategies.integers(), strategies.floats()),
    b=strategies.one_of(strategies.integers(), strategies.floats()),
)
def test_mysum(a, b):
    my_sum(a, b)


# negativer Test, text und email kann man nicht summieren!
@given(
    a=strategies.text(),
    b=strategies.emails(),
)
def test_mysum(a, b):
    with pytest.raises(ValueError):
        my_sum(a, b)


if __name__ == "__main__":
    print(my_sum(1, 3))
    print(my_sum("1", "3"))

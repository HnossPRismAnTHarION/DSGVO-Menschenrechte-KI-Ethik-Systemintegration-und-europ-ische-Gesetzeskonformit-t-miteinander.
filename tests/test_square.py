from square import square


def test_square_positive():
    assert square(4) == 16


def test_square_negative():
    assert square(-3) == 9


def test_square_float():
    assert square(2.5) == 6.25

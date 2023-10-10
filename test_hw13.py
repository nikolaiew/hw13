def square(a):
    return a * a


def test_positive():
    assert square(2) == 4


def test_negative():
    assert (not square(3) < 9) and (not square(3) > 9)



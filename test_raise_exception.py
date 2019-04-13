from pytest import raises


def raise_exception():
    raise ValueError


def test_raise_except():
    with raises(ValueError):
        raise_exception()
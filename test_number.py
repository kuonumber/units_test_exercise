from pytest import approx


def test_number():
    repr('用近似方法解決浮點數問題')
    assert (0.1 + 0.2) == approx(0.3)
import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    repr('have to use request as parameter')
    setup_attributes = request.param
    print('this is {}'.format(setup_attributes))
    print('hello world')


def test_1(setup):
    print('I am test 1')
    assert True


@pytest.mark.usefixtures("setup")
def test_2():
    print('I am test 2')
import random

import pytest


@pytest.fixture(scope='session')
def browser():
    print(random.randint(0, 100))
    print('open browser')
    yield 'Chrome'
    print('close browser')


@pytest.fixture
def get_admin(browser):
    return random.randint(0, 100)


def test_simple(get_admin, browser):
    assert get_admin == 5, 'ждём 5'
    assert browser == 'Chrome'
    assert 1 == 1, 'единица не равна двлйке'


def test_another(browser_two, get_admin):
    assert get_admin == 5, 'ждём 5'
    assert 1 == 1, 'единица не равна двлйке'

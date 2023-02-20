import pytest


@pytest.fixture
def browser_two():
    print('open browser')
    yield 'Yandex'
    print('close browser')
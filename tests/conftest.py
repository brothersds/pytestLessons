import pytest


@pytest.fixture()
def set_up():
    print("\nВход в систему выполнен")
    yield
    print("\nВыход из системы")


@pytest.fixture(scope="module")
def some():
    print("\nНачало")
    yield
    print("\nКонец")

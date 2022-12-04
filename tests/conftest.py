import pytest


@pytest.fixture()
def set_up():
    print("\nВход в систему выполнен")
    yield
    print("\nВыход из системы")

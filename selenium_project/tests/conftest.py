import pytest

@pytest.fixture()
def set_up():
    print("\nНачало теста")
    yield
    print("\nОкончание теста")

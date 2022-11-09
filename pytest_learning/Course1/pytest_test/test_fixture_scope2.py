import pytest

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("Setup Module2")

@pytest.fixture(scope="class", autouse=True)
def setupSession():
    print("Setup Class2")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("Setup Function2")

class TestClass:
    def test_it(self):
        print("TestIt")
        assert True

    def test_it2(self):
        print("TestIt2")
        assert True
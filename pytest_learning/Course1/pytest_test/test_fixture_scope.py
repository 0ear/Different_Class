import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("Setup Session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("Setup Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("Setup Function")

def test1():
    print("Executine test1!")
    assert True

def test2():
    print("Executine test2!")
    assert True
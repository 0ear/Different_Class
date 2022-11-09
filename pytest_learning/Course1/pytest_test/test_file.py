def test_me():
    assert True


def test_me2():
    assert True


def not_a_test():
    assert True

class MyTestClass():
    #此class會被略過
    def test_it(self):
        assert True

    def test_it2(self):
        assert True


class TestClass():
    def test_me(self):
        assert True

    def test_me2(self):
        assert True
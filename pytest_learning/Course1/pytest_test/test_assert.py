from pytest import approx
from pytest import raises

def test_InAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_floatAssert():
    assert 1.0 == 1.0

def test_arrayAssert():
    assert [1,2,3] == [1,2,3]

def test_dictAssert():
    assert {'1':1} == {'1':1}

def test_float():
    # assert (0.1+0.2) == 0.3 會報錯
    #需要用
    assert (0.1 + 0.2) == approx(0.3)

def raiseValueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raiseValueException()
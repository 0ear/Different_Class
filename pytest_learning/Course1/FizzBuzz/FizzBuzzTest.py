import pytest

#fizzBuzz 具體想要達成的邏輯寫在Use case的file裡

def test_canAssertTrue():
    assert True

def fizzBuzz(value):
    if isMUltiple(value, 3):
        if isMUltiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMUltiple(value, 5):
        return "Buzz"
    return str(value)

def checkFizzBuzz(value, expectedRetVal):
    """
    下面兩test,做的事差不多,因此只需要一個func去表達其內部做的事即可
    """
    retval = fizzBuzz(value)
    assert retval == expectedRetVal

def isMUltiple(value, mod):
    """
    上面 fizzBuzz內的判斷又有重複部分, 因此用一func處理
    """
    return (value % mod) == 0

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")
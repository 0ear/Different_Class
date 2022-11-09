import pytest

from Checkout import Checkout

# 因為跟下面的重複了所以可以拔掉了
# def test_CanInstantiateCheckout():
#     co = Checkout()
# def test_CanAddItemPrice(checkout):
#     checkout.addItemPrice("a", 1)
#
# def test_CanAddItem(checkout):
#     checkout.addItem("a")

@pytest.fixture()
def checkout():
    """
    改寫下面需要每個test重複建Checkout物件
    """
    checkout = Checkout()
    #下面測試重複用到部分就加入
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout


def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)

#為了要pass這個test所以前面要大改, 因此先讓此處test略過, 並確定接下來的更改能過前面的test
#@pytest.mark.skip 當前面都過了要來測試這裡時才註解掉這個
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c") #c沒有先給過價格
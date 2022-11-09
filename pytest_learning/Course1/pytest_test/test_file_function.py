#Module會在執行此file的最前和最後執行
def setup_module(module):
    print("Setup Module!")

def teardown_module(module):
    print("Teardowm Module!")

def setup_function(function):
    if function == test1:
        print("\nSetting up test1!")
    elif function == test2:
        print("\nSetting up test2!")
    else:
        print("\nSetting up unknown test!")

def teardown_function(function):
    if function == test1:
        print("\nTearing down test1!")
    elif function == test2:
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")

#執行順序會是先執行setup -> test1 -> teardown -> setup2 -> test2 -> teardown2
def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True
import json

from pytest import fixture
from selenium import webdriver

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file) #讀進來是一個list
        return data

@fixture(params=[webdriver.Chrome,
                 webdriver.Firefox, #電腦沒有firefox所以會報錯
                 webdriver.Edge]
         )
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

data_path = "./class4/tests/test_data.json"

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
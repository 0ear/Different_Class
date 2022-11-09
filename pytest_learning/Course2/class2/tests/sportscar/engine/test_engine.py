import pytest
from selenium import webdriver


@pytest.mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('https://www.artofmanliness.com/articles/how-a-cars-engine-works/')
    assert True

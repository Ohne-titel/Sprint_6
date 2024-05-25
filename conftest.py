import pytest
from selenium import webdriver
from config import URL


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(URL)
    driver.maximize_window()

    yield driver

    driver.quit()

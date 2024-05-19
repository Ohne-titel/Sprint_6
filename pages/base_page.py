import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from config import URL
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие стартовой страницы')
    def open_page(self, driver):
        self.driver.get(URL)

    @allure.step('Принятие куки')
    def get_cookies(self, driver):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(BasePageLocators.cookie_button)).click()




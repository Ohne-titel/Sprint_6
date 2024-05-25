import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    COOCKIE_BUTTON = (By.XPATH, "//*[@id='rcc-confirm-button']")  # кнопка принятия куки

    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    def find_element_and_click(self, locator):
        self.find_element_located(locator).click()

    def get_cookie(self):
        self.find_element_and_click(self.COOCKIE_BUTTON)

    @allure.step('Видимость элемента')
    def visibility_of_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание урла')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    @allure.step('Получение текущего урла')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получение урла после редиректа')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

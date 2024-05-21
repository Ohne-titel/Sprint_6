import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from config import URL
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие стартовой страницы')
    def open_page(self):
        self.driver.get(URL)

    @allure.step('Принятие куки')
    def get_cookies(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(BasePageLocators.cookie_button)).click()

    @allure.step('Клик список вопросов')
    def visibility_question_list(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(BasePageLocators.question_list))

    @allure.step('Клик по каждому вопросу по локатору')
    def click_question(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Клик по каждому ответу по локатору')
    def click_answer(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Клик по логотипу "Яндекса"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.yandex_logo).click()

    @allure.step('Клик по логотипу "Самоката"')
    def click_samokat_logo(self):
        self.driver.find_element(*BasePageLocators.samokat_logo).click()

    @allure.step('Клик на кнопку "Заказать" в шапке ')
    def click_top_button(self):
        self.driver.find_element(*BasePageLocators.top_order_button_selector).click()

    @allure.step('Ожидание урла')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    @allure.step('Получение текущего урла')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получение урла после редиректа')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание списка вопросов')
    def visibility_question_list(self):
        self.visibility_of_element(MainPageLocators.question_list)

    @allure.step('Клик по каждому вопросу по локатору')
    def click_question(self, locator):
        self.find_element_located(locator).click()

    @allure.step('Клик по каждому ответу по локатору')
    def get_answer(self, locator):
        return self.find_element_located(locator).text

    @allure.step('Клик по логотипу "Яндекса"')
    def click_yandex_logo(self):
        self.find_element_located(MainPageLocators.yandex_logo).click()

    @allure.step('Клик по логотипу "Самоката"')
    def click_samokat_logo(self):
        self.find_element_located(MainPageLocators.samokat_logo).click()

    @allure.step('Клик на кнопку "Заказать" в шапке ')
    def click_top_button(self):
        self.find_element_located(MainPageLocators.top_order_button_selector).click()








import allure
import pytest
from selenium import webdriver
from conftest import driver
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestQuestionsList:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'question, answer, text_answer',
        [
            (BasePageLocators.question_1, BasePageLocators.answer_1, 'Сутки — 400 рублей. Оплата курьеру — наличными '
                                                                     'или картой.'),
            (BasePageLocators.question_2, BasePageLocators.answer_2, 'Пока что у нас так: один заказ — один самокат. '
                                                                     'Если хотите покататься с друзьями, '
                                                                     'можете просто сделать несколько заказов — один '
                                                                     'за другим.'),
            (BasePageLocators.question_3, BasePageLocators.answer_3, 'Допустим, вы оформляете заказ на 8 мая. Мы '
                                                                     'привозим самокат 8 мая в течение дня. Отсчёт '
                                                                     'времени аренды начинается с момента, '
                                                                     'когда вы оплатите заказ курьеру. Если мы '
                                                                     'привезли самокат 8 мая в 20:30, суточная аренда '
                                                                     'закончится 9 мая в 20:30.'),
            (BasePageLocators.question_4, BasePageLocators.answer_4, 'Только начиная с завтрашнего дня. Но скоро '
                                                                     'станем расторопнее.'),
            (BasePageLocators.question_5, BasePageLocators.answer_5, 'Пока что нет! Но если что-то срочное — всегда '
                                                                     'можно позвонить в поддержку по красивому номеру'
                                                                     ' 1010.'),
            (BasePageLocators.question_6, BasePageLocators.answer_6, 'Самокат приезжает к вам с полной зарядкой. '
                                                                     'Этого хватает на восемь суток — даже если '
                                                                     'будете кататься без передышек и во сне. Зарядка '
                                                                     'не понадобится.'),
            (BasePageLocators.question_7, BasePageLocators.answer_7, 'Да, пока самокат не привезли. Штрафа не будет, '
                                                                     'объяснительной записки тоже не попросим. Все же'
                                                                     ' свои.'),
            (BasePageLocators.question_8, BasePageLocators.answer_8, 'Да, обязательно. Всем самокатов! И Москве, '
                                                                     'и Московской области.')
        ]
    )
    @allure.title('Проверка соответствия текста ответов на вопросы')
    def test_question_list(self, question, answer, text_answer, driver):
        base_page = BasePage(driver)
        base_page.open_page(self)
        base_page.get_cookies(self)
        main_page = MainPage(driver)
        main_page.visibility_question_list()
        main_page.click_question(question)
        real_answer = main_page.click_answer(answer)
        assert real_answer == text_answer


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
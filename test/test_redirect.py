import allure
from selenium import webdriver
from conftest import driver
from config import URL, DZEN_HOME_PAGE
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestRedirect:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Переход по клику на кнопку Самокат')
    def test_click_samokat_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(self)
        main_page = MainPage(driver)
        main_page.click_top_button(driver)
        main_page.click_samokat_logo()
        main_page.wait_for_url(URL, driver)
        main_page_url = URL
        assert main_page_url == main_page.get_current_url()

    @allure.title('Переход по клику на кнопку Яндекс')
    def test_click_yandex_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(self)
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_window()
        main_page.wait_for_url(DZEN_HOME_PAGE, driver)
        dzen_url = DZEN_HOME_PAGE
        assert dzen_url == main_page.get_current_url()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

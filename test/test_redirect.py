import allure
from conftest import driver
from config import URL, DZEN_HOME_PAGE
from pages.main_page import MainPage


class TestRedirect:

    @allure.title('Переход по клику на кнопку Самокат')
    def test_click_samokat_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_button()
        main_page.click_samokat_logo()
        main_page.wait_for_url(URL)
        base_page_url = URL
        assert base_page_url == main_page.get_current_url()

    @allure.title('Переход по клику на кнопку Яндекс')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_window()
        main_page.wait_for_url(DZEN_HOME_PAGE)
        dzen_url = DZEN_HOME_PAGE
        assert dzen_url == main_page.get_current_url()

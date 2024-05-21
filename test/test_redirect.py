import allure
from conftest import driver
from config import URL, DZEN_HOME_PAGE
from pages.base_page import BasePage


class TestRedirect:

    @allure.title('Переход по клику на кнопку Самокат')
    def test_click_samokat_logo(self, driver):
        base_page = BasePage(driver)
        base_page.click_top_button()
        base_page.click_samokat_logo()
        base_page.wait_for_url(URL)
        base_page_url = URL
        assert base_page_url == base_page.get_current_url()

    @allure.title('Переход по клику на кнопку Яндекс')
    def test_click_yandex_logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_page()
        base_page.click_yandex_logo()
        base_page.switch_to_window()
        base_page.wait_for_url(DZEN_HOME_PAGE)
        dzen_url = DZEN_HOME_PAGE
        assert dzen_url == base_page.get_current_url()

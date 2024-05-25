import allure
import pytest
from conftest import driver
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        'name, lastname, address, telephone',
        [
            ['Лина', 'Мягкова', 'Воронеж, ул.Энгельса, 22', '89999999999'],
        ]
    )
    @allure.title('Оформление заказа через верхнюю кнопку "Заказать"')
    def test_order_top_button(self, driver, name, lastname, address, telephone):
        order_page = OrderPage(driver)
        order_page.click_top_order_button()
        order_page.set_name(name)
        order_page.set_lastname(lastname)
        order_page.set_address(address)
        order_page.set_metro_station()
        order_page.set_telephone(telephone)
        order_page.create_order_with_parametrize()

        text = order_page.order_placed_success()
        assert 'Заказ оформлен' in text

    @pytest.mark.parametrize(
        'name, lastname, address, telephone',
        [
            ['Лина', 'Кистер', 'Москва, Котельническая набережная, 11', '89000000000']
        ]
    )
    @allure.title('Оформление заказа через нижнюю кнопку "Заказать"')
    def test_order_bottom_button(self, driver, name, lastname, address, telephone):
        order_page = OrderPage(driver)
        order_page.get_cookie()
        order_page.click_bottom_order_button()
        order_page.set_name(name)
        order_page.set_lastname(lastname)
        order_page.set_address(address)
        order_page.set_metro_station()
        order_page.set_telephone(telephone)
        order_page.create_order_with_parametrize()

        text = order_page.order_placed_success()
        assert 'Заказ оформлен' in text

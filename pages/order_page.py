import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на кнопку "Заказать" в шапке ')
    def click_top_order_button(self):
        self.find_element_located(OrderPageLocators.top_order_button_selector).click()

    @allure.step('Клик на кнопку "Заказать" в середине страницы ')
    def click_bottom_order_button(self):
        self.find_element_located(OrderPageLocators.bottom_order_button_selector).click()

    @allure.step('Ввод имени')
    def set_name(self, name):
        self.find_element_located(OrderPageLocators.name_selector).send_keys(name)

    @allure.step('Ввод фамилии')
    def set_lastname(self, lastname):
        self.find_element_located(OrderPageLocators.lastname_selector).send_keys(lastname)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.find_element_located(OrderPageLocators.address_selector).send_keys(address)

    @allure.step('Выбор станции метро')
    def set_metro_station(self):
        station_list = self.find_element_located(OrderPageLocators.metro_list)
        station_list.click()
        metro_station = self.find_element_located(OrderPageLocators.metro_station)
        metro_station.click()

    @allure.step('Ввод номера телефона')
    def set_telephone(self, telephone):
        self.find_element_located(OrderPageLocators.telephone_number).send_keys(telephone)

    @allure.step('Кнопка "Далее"')
    def click_next_step_button(self):
        self.find_element_located(OrderPageLocators.next_step).click()

    @allure.step('Выбор даты')
    def set_date(self):
        self.find_element_located(OrderPageLocators.date_selector).click()
        self.find_element_located(OrderPageLocators.choose_date).click()

    @allure.step('Выбор срока аренды')
    def set_rental_period(self):
        rental_period = self.find_element_located(OrderPageLocators.period_field)
        rental_period.click()
        choose_period = self.find_element_located(OrderPageLocators.day_order)
        choose_period.click()

    @allure.step('Выбор цвета')
    def set_color(self):
        self.find_element_located(OrderPageLocators.color).click()
        self.find_element_located(OrderPageLocators.color_checkbox).click()

    @allure.step('Подтверждение заказа')
    def order(self):
        self.find_element_located(OrderPageLocators.order_button).click()
        self.find_element_located(OrderPageLocators.confirm_order).click()

    @allure.step('Заказ оформлен')
    def order_placed_success(self):
        return self.find_element_located(OrderPageLocators.order_placed_window).text

    @allure.step('Комбинация методов (шаги)')
    def create_order_with_parametrize(self):
        self.click_next_step_button()
        self.set_date()
        self.set_rental_period()
        self.set_color()
        self.order()
        self.order_placed_success()

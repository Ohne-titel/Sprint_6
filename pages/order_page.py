import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на кнопку "Заказать" в шапке ')
    def click_top_order_button(self, driver):
        self.driver.find_element(*OrderPageLocators.top_order_button_selector).click()

    @allure.step('Клик на кнопку "Заказать" в середине страницы ')
    def click_bottom_order_button(self, driver):
        self.driver.find_element(*OrderPageLocators.bottom_order_button_selector).click()

    @allure.step('Ввод имени')
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_selector).send_keys(name)

    @allure.step('Ввод фамилии')
    def set_lastname(self, lastname):
        self.driver.find_element(*OrderPageLocators.lastname_selector).send_keys(lastname)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_selector).send_keys(address)

    @allure.step('Выбор станции метро')
    def set_metro_station(self):
        station_list = self.driver.find_element(*OrderPageLocators.metro_list)
        station_list.click()
        metro_station = self.driver.find_element(*OrderPageLocators.metro_station)
        metro_station.click()

    @allure.step('Ввод номера телефона')
    def set_telephone(self, telephone):
        self.driver.find_element(*OrderPageLocators.telephone_number).send_keys(telephone)

    @allure.step('Кнопка "Далее"')
    def click_next_step_button(self):
        self.driver.find_element(*OrderPageLocators.next_step).click()

    @allure.step('Выбор даты')
    def set_date(self):
        self.driver.find_element(*OrderPageLocators.date_selector).click()
        self.driver.find_element(*OrderPageLocators.choose_date).click()

    @allure.step('Выбор срока аренды')
    def set_rental_period(self):
        rental_period = self.driver.find_element(*OrderPageLocators.period_field)
        rental_period.click()
        choose_period = self.driver.find_element(*OrderPageLocators.day_order)
        choose_period.click()

    @allure.step('Выбор цвета')
    def set_color(self):
        self.driver.find_element(*OrderPageLocators.color).click()
        self.driver.find_element(*OrderPageLocators.color_checkbox).click()

    @allure.step('Подтверждение заказа')
    def order(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()
        self.driver.find_element(*OrderPageLocators.confirm_order).click()

    @allure.step('Заказ оформлен')
    def order_placed_success(self):
        return self.driver.find_element(*OrderPageLocators.order_placed_window).text

    @allure.step('Комбинация методов (шаги)')
    def create_order_with_parametrize(self):
        self.click_next_step_button()
        self.set_date()
        self.set_rental_period()
        self.set_color()
        self.order()
        self.order_placed_success()

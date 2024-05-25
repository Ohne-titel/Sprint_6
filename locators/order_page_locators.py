from selenium.webdriver.common.by import By


class OrderPageLocators:
    top_order_button_selector = (By.XPATH, "//*[@class='Button_Button__ra12g']")  # верхняя кнопка "Заказать"
    bottom_order_button_selector = (
        By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")  # нижняя кнопка "Заказать"
    name_selector = (By.XPATH, "//input[@placeholder='* Имя']")   # строка "Имя"
    lastname_selector = (By.XPATH, "//input[@placeholder = '* Фамилия']")   # строка "Фамилия
    address_selector = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")   # строка "Адрес"
    metro_list = (By.XPATH, "//input[@placeholder='* Станция метро']")   # дропдаун "Станция метро"
    metro_station = (By.XPATH, '//li[@data-value="1"]')  # выбор станции метро
    telephone_number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")   # строка "Телефон"
    next_step = (By.XPATH, "//button[contains(.,'Далее')]")   # кнопка "Далее"
    date_selector = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")   # строка даты
    choose_date = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--029 "
                             "react-datepicker__day--outside-month']")  # выбранная дата
    period_field = (By.XPATH, "//div[text()='* Срок аренды']")  # строка "Когда привезти самокат"
    day_order = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")   # дата в дропдауне
    color = (By.XPATH, "//div[@class='Order_Checkboxes__3lWSI']")    # строка "Выбор цвета"
    color_checkbox = (By.XPATH, ".//label[text() = 'чёрный жемчуг']/input")   # выбранный цвет
    order_button = (By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']")   # кнопка "Заказать"
    confirm_order = (By.XPATH, "//button[contains(.,'Да')]")   # кнопка "Да"
    order_placed_window = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")   # окно успешного заказа


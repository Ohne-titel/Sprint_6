from selenium.webdriver.common.by import By


class MainPageLocators:
    question_list = (By.XPATH, "//div[@class='Home_FourPart__1uthg']")  # локатор вопросов выпадющего списка
    question_1 = (By.XPATH, "//div[@id='accordion__heading-0']")  # локатор вопроса №1
    question_2 = (By.XPATH, "//div[@id='accordion__heading-1']")  # локатор вопроса №2
    question_3 = (By.XPATH, "//div[@id='accordion__heading-2']")  # локатор вопроса №3
    question_4 = (By.XPATH, "//div[@id='accordion__heading-3']")  # локатор вопроса №4
    question_5 = (By.XPATH, "//div[@id='accordion__heading-4']")  # локатор вопроса №5
    question_6 = (By.XPATH, "//div[@id='accordion__heading-5']")  # локатор вопроса №6
    question_7 = (By.XPATH, "//div[@id='accordion__heading-6']")  # локатор вопроса №7
    question_8 = (By.XPATH, "//div[@id='accordion__heading-7']")  # локатор вопроса №8
    answer_1 = (By.XPATH, "//div[@id='accordion__panel-0']")  # локатор ответа №1
    answer_2 = (By.XPATH, "//div[@id='accordion__panel-1']")  # локатор ответа №2
    answer_3 = (By.XPATH, "//div[@id='accordion__panel-2']")  # локатор ответа №3
    answer_4 = (By.XPATH, "//div[@id='accordion__panel-3']")  # локатор ответа №4
    answer_5 = (By.XPATH, "//div[@id='accordion__panel-4']")  # локатор ответа №5
    answer_6 = (By.XPATH, "//div[@id='accordion__panel-5']")  # локатор ответа №6
    answer_7 = (By.XPATH, "//div[@id='accordion__panel-6']")  # локатор ответа №7
    answer_8 = (By.XPATH, "// div[ @ id = 'accordion__panel-7']")  # локатор ответа №8

    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")  # логотип "Яндекс"
    samokat_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")  # логотип "Самокат"
    top_order_button_selector = (By.XPATH, "//*[@class='Button_Button__ra12g']")  # верхняя кнопка "Заказать"
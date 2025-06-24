from selenium.webdriver.common.by import By

class LocatorsMainPage:
    # локаторы для кнопок "заказать"
    order_button_header = (By.CLASS_NAME,'Button_Button__ra12g')
    order_button_middle = (By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]")

    # локаторы для логотипов "Яндекс" и "Самокат"
    logo_yandex = (By.CLASS_NAME,'Header_LogoYandex__3TSOI')
    logo_scooter = (By.CLASS_NAME,'Header_LogoScooter__3lsAR')

    # локатор для вопросов
    questions_section = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    questions = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7')
    ]
    # локатор для ответов
    answer = [
        (By.ID, 'accordion__panel-0'),
        (By.ID, 'accordion__panel-1'),
        (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'),
        (By.ID, 'accordion__panel-4'),
        (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'),
        (By.ID, 'accordion__panel-7')
    ]
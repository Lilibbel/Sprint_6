from selenium.webdriver.common.by import By

class LocatorsOrderPage:
    # локаторы для логотипов "Яндекс" и "Самокат"
    logo_yandex = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    logo_scooter = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    # локаторы для 1 части формы заказа
    name = (By.XPATH, '//input[@placeholder="* Имя"]')
    last_name = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    metro_list = (By.CLASS_NAME, "select-search__row")
    phone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    button_next = (By.XPATH, "//button[text()='Далее']")

    # локаторы для 2 части формы заказа
    date_input = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    period = (By.CLASS_NAME, 'Dropdown-placeholder')
    period_list = (By.XPATH, '//div[@class="Dropdown-menu"]')
    color_black = (By.ID, 'black')
    color_grey = (By.ID, 'grey')
    comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    back_button = (By.CSS_SELECTOR, 'button.Button_Button__ra12g Button_Middle__1CSJM.Button_Inverted__3IF-i')
    order_modal = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    button_yes = (By.XPATH, "//button[text()='Да']")
    button_no = (By.XPATH, "//button[text()='Нет']")
    model_order_placed = (By.XPATH, "//button[text()='Заказ оформлен']" )
    button_status = (By.XPATH, "//button[text()='Посмотреть статус']" )





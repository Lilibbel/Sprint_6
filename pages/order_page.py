import allure
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_locators import LocatorsOrderPage

class OrderPage(BasePage):

    @allure.step('Подождать подгрузки поля "имя"')
    def wait_visibility_name(self):
        self.wait_visibility_of_element(LocatorsOrderPage.name)

    @allure.step("Заполнить первую форму")
    def send_first_form_to_input(self, keys):
        self.send_keys_to_input(LocatorsOrderPage.name, keys[0])
        self.send_keys_to_input(LocatorsOrderPage.last_name, keys[1])
        self.send_keys_to_input(LocatorsOrderPage.address, keys[2])
        self.send_keys_to_input(LocatorsOrderPage.metro, keys[3])
        station_locator = (By.XPATH, f'//*[contains(text(), "{keys[3]}")]')
        self.click_on_element(station_locator)
        self.send_keys_to_input(LocatorsOrderPage.phone, keys[4])

    @allure.step('Кликнуть на кнопку "Далее"')
    def click_on_button_next(self):
        self.click_on_element(LocatorsOrderPage.button_next)

    @allure.step("Заполнить вторую форму")
    def send_second_form_to_input(self, keys):
        self.wait_visibility_of_element(LocatorsOrderPage.date_input)
        self.send_keys_to_input(LocatorsOrderPage.date_input, keys[5])
        self.click_on_element((By.XPATH, "//div[contains(text(), 'Про аренду')]"))
        self.click_on_element(LocatorsOrderPage.period)
        period_locator = (By.XPATH,f'//*[contains(text(), "{keys[6]}")]')
        self.click_on_element(period_locator)
        self.click_on_element(LocatorsOrderPage.color_black)
        self.send_keys_to_input(LocatorsOrderPage.comment, keys[7])

    @allure.step('Кликнуть на цвет "чёрный жемчуг"')
    def click_on_color_black(self):
        self.click_on_element(LocatorsOrderPage.color_black)

    @allure.step('Кликнуть на цвет "серая безысходность"')
    def click_on_color_grey(self):
        self.click_on_element(LocatorsOrderPage.color_grey)

    @allure.step("Ввести значение в поле комментарий курьеру")
    def send_comment_to_input(self, keys):
        self.send_keys_to_input(LocatorsOrderPage.comment, keys)

    @allure.step('Кликнуть на кнопку "Назад"')
    def click_on_back_button(self):
        self.click_on_element(LocatorsOrderPage.back_button)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_on_order_button(self):
        self.click_on_element(LocatorsOrderPage.order_button)

    @allure.step('Подождать прогрузки окна подтверждения заказа')
    def wait_visibility_of_order_modal(self):
        self.wait_visibility_of_element(LocatorsOrderPage.order_modal)

    @allure.step('Кликнуть на кнопку "Нет"')
    def click_on_button_no(self):
        self.click_on_element(LocatorsOrderPage.button_no)

    @allure.step('Кликнуть на кнопку "Да"')
    def click_on_button_yes(self):
        self.click_on_element(LocatorsOrderPage.button_yes)

    @allure.step('Подождать прогрузки окна "заказа оформлен"')
    def wait_visibility_of_order_placed_modal(self):
        self.wait_visibility_of_element(LocatorsOrderPage.model_order_placed)

    @allure.step('Проверить отображение кнопки "Посмотреть статус')
    def button_status_displayed(self):
        return self.is_element_displayed(LocatorsOrderPage.button_status)

    @allure.step('Кликнуть на кнопку "Посмотреть статус"')
    def click_on_button_status(self):
        self.click_on_element(LocatorsOrderPage.button_status)

    @allure.step('Подождать подгрузки логотипа Яндекс')
    def wait_visibility_logo_yandex(self):
        self.wait_visibility_of_element(LocatorsOrderPage.logo_yandex)

    @allure.step('Подождать подгрузки логотипа Самокат')
    def wait_visibility_logo_scooter(self):
        self.wait_visibility_of_element(LocatorsOrderPage.logo_scooter)

    @allure.step('Клик по логотипу Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(LocatorsOrderPage.logo_yandex)

    @allure.step('Клик по логотипу Самокат')
    def click_on_logo_scooter(self):
        self.click_on_element(LocatorsOrderPage.logo_scooter)
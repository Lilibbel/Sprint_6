from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage
from locators.main_locators import LocatorsMainPage

class MainPage(BasePage):

    @allure.step('Подождать подгрузки кнопки "заказать" в header')
    def wait_visibility_order_button_header(self):
        self.wait_visibility_of_element(LocatorsMainPage.order_button_header)

    @allure.step('Подождать подгрузки кнопки "заказать" внизу страницы')
    def wait_visibility_order_button_middle(self):
        self.wait_visibility_of_element(LocatorsMainPage.order_button_middle)

    @allure.step('Подождать подгрузки логотипа Яндекс')
    def wait_visibility_logo_yandex(self):
        self.wait_visibility_of_element(LocatorsMainPage.logo_yandex)

    @allure.step('Подождать подгрузки логотипа Самокат')
    def wait_visibility_logo_scooter(self):
        self.wait_visibility_of_element(LocatorsMainPage.logo_scooter)

    @allure.step('Клик по кнопке "Заказать" в header')
    def click_on_order_button_header(self):
        self.click_on_element(LocatorsMainPage.order_button_header)

    @allure.step('Проскролить до кнопки "Заказать" внизу страницы')
    def scroll_to_order_button_middle(self):
        self.scroll_to_element(LocatorsMainPage.order_button_middle)

    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_on_order_button_middle(self):
        self.click_on_element(LocatorsMainPage.order_button_middle)

    @allure.step('Клик по логотипу Яндекс')
    def click_on_logo_yandex(self):
        self.click_on_element(LocatorsMainPage.logo_yandex)

    @allure.step('Клик по логотипу Самокат')
    def click_on_logo_scooter(self):
        self.click_on_element(LocatorsMainPage.logo_scooter)

    @allure.step('Проскролить до вопросов')
    def scroll_to_questions(self):
        self.scroll_to_element(LocatorsMainPage.questions_section)

    @allure.step('Подождать подгрузки вопроса под номером')
    def wait_visibility_question_nomber(self, number):
        self.wait_visibility_of_element(LocatorsMainPage.questions[number])

    @allure.step('Клик по вопросу под номером')
    def click_on_question_nomber(self, number):
        self.scroll_to_element(LocatorsMainPage.questions[number])
        self.click_on_element(LocatorsMainPage.questions[number])

    @allure.step('Подождать подгрузки ответа на вопрос под номером')
    def wait_visibility_answer_nomber(self, number):
        self.wait_visibility_of_element(LocatorsMainPage.answer[number])

    @allure.step('Проверить отображение ответа под номером')
    def is_answer_displayed(self, number):
        return self.is_element_displayed(LocatorsMainPage.answer[number])

    @allure.step('Получить текст ответа под номером')
    def get_text_on_answer(self, number):
        return self.get_text_on_element(LocatorsMainPage.answer[number])


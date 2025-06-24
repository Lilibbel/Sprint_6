import allure
import pytest
from pages.order_page import OrderPage
from data import TestData
from locators.main_locators import LocatorsMainPage

class TestOrderCreation:

    @allure.title('Проверка оформления заказа')
    @allure.description('Сквозное тестирование функциональности оформления заказа')
    @pytest.mark.parametrize('button, test_data', [
        (LocatorsMainPage.order_button_header, TestData.user_1),
        (LocatorsMainPage.order_button_middle, TestData.user_2)
    ])
    def test_order_creation(self, driver, button, test_data):
        order_page  = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.wait_visibility_name()
        order_page.send_first_form_to_input(test_data)
        order_page.click_on_button_next()
        order_page.send_second_form_to_input(test_data)
        order_page.click_on_order_button()
        order_page.wait_visibility_of_order_modal()
        order_page.click_on_button_yes()
        order_page.wait_visibility_of_order_placed_modal
        assert order_page.button_status_displayed()
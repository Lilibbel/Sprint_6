import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature('Проверка логотипов на главной странице')
class TestLogosMain:
    @allure.title('Проверка перехода на главную страницу при клике на логотип Самоката')
    def test_scooter_logo_redirect_main(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_scooter()
        WebDriverWait(driver, 10).until(EC.url_to_be(TestData.base_url))
        assert driver.current_url == TestData.base_url

    @allure.title('Проверка перехода на Дзен при клике на логотип Яндекса')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        main_page.switch_to_dzen_window()
        WebDriverWait(driver, 20).until(EC.url_contains('dzen.ru'))
        assert 'dzen.ru' in main_page.driver.current_url.lower()

@allure.feature('Проверка логотипов на странице заказа')
class TestLogosOrder:
    @allure.title('Проверка перехода на главную страницу при клике на логотип Самоката')
    def test_scooter_logo_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_logo_scooter()
        WebDriverWait(driver, 10).until(EC.url_to_be(TestData.base_url))
        assert order_page.driver.current_url == TestData.base_url

    @allure.title('Проверка перехода на Дзен при клике на логотип Яндекса')
    def test_yandex_logo_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_logo_yandex()
        order_page.switch_to_dzen_window()
        WebDriverWait(driver, 20).until(EC.url_contains('dzen.ru'))
        assert 'dzen.ru' in order_page.driver.current_url.lower()
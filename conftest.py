import pytest
from selenium import webdriver
from data import TestData
from pages.main_page import MainPage
from pages.order_page import OrderPage

# Фикстура для инициализации и закрытия Firefox
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(TestData.base_url)

    yield driver
    driver.quit()
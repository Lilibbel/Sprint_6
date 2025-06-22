from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить заголовок текущей страницы')
    def get_page_title(self):
        self.driver.title

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Проверить отображение элемента')
    def is_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Ввести значение в поле ввода")
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Перейти на другую вкладку')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self

    @allure.step('Перейти на вкладку Дзен')
    def switch_to_dzen_window(self):
        self.switch_to_last_window()
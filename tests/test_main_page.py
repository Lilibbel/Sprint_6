import allure
import pytest
from pages.main_page import MainPage
from data import TestData


@allure.feature('Проверка раздела "Вопросы о важном"')
class TestQuestionsSection:
    @allure.title('Проверка ответа на вопрос №{question_num+1}')
    @pytest.mark.parametrize('question_num, expected_answer', [
        (0, TestData.question_answer[0]),
        (1, TestData.question_answer[1]),
        (2, TestData.question_answer[2]),
        (3, TestData.question_answer[3]),
        (4, TestData.question_answer[4]),
        (5, TestData.question_answer[5]),
        (6, TestData.question_answer[6]),
        (7, TestData.question_answer[7])
    ])
    def test_question_answer(self, driver, question_num, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_on_question_nomber(question_num)
        main_page.wait_visibility_answer_nomber(question_num)
        assert main_page.is_answer_displayed(question_num), f"Ответ на вопрос №{question_num + 1} не отображается"
        actual_answer = main_page.get_text_on_answer(question_num)
        assert actual_answer == expected_answer, \
            f"Неверный текст ответа для вопроса №{question_num + 1}\nОжидалось: {expected_answer}\nФактически: {actual_answer}"



@allure.feature('Проверка кнопок "Заказать"')
class TestOrderButtons:
    @allure.title('Проверка открытия формы заказа при клике на кнопку "Заказать" в хедере')
    def test_order_button_header_opens_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_button_header()
        assert "order" in driver.current_url.lower()

    @allure.title('Проверка открытия формы заказа при клике на кнопку "Заказать" внизу страницы')
    def test_order_button_middle_opens_form(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_order_button_middle()
        main_page.click_on_order_button_middle()
        assert "order" in driver.current_url.lower()
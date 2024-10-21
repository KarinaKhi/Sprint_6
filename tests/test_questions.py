import time
from pages.questions_page import QuestionsBox
from conftest import *


class TestImportantQuestions:

    def test_first_question(self, driver, open_main_page, question_index=0):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на первый вопрос не отображается"

    def test_second_question(self, driver, open_main_page, question_index=1):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на второй вопрос не отображается"

    def test_third_question(self, driver, open_main_page, question_index=2):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на третий вопрос не отображается"

    def test_fourth_question(self, driver, open_main_page, question_index=3):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на четвертый вопрос не отображается"

    def test_fifth_question(self, driver, open_main_page, question_index=4):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        time.sleep(1)
        assert questions_box.is_answer_visible(question_index), "Ответ на пятый вопрос не отображается"

    def test_sixth_question(self, driver, open_main_page, question_index=5):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        time.sleep(1)
        assert questions_box.is_answer_visible(question_index), "Ответ на шестой вопрос не отображается"

    def test_seventh_question(self, driver, open_main_page, question_index=6):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        time.sleep(1)
        assert questions_box.is_answer_visible(question_index), "Ответ на седьмой вопрос не отображается"

    def test_eight_question(self, driver, open_main_page, question_index=7):
        questions_box = QuestionsBox(driver)
        questions_box.click_question(question_index)
        time.sleep(1)
        assert questions_box.is_answer_visible(question_index), "Ответ на восьмой вопрос не отображается"

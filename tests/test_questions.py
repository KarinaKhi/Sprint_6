import pytest
from selenium import webdriver
from pages.questions_page import QuestionsBox


class TestImportantQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru')

    @pytest.mark.parametrize("question_index", [0])
    def test_first_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на первый вопрос не отображается"

    @pytest.mark.parametrize("question_index", [1])
    def test_second_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на второй вопрос не отображается"

    @pytest.mark.parametrize("question_index", [2])
    def test_third_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на третий вопрос не отображается"

    @pytest.mark.parametrize("question_index", [3])
    def test_fourth_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на четвертый вопрос не отображается"

    @pytest.mark.parametrize("question_index", [4])
    def test_fifth_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на пятый вопрос не отображается"

    @pytest.mark.parametrize("question_index", [5])
    def test_sixth_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на шестой вопрос не отображается"

    @pytest.mark.parametrize("question_index", [6])
    def test_seventh_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на седьмой вопрос не отображается"

    @pytest.mark.parametrize("question_index", [7])
    def test_eight_question(self, question_index):
        questions_box = QuestionsBox(self.driver)
        questions_box.click_question(question_index)
        assert questions_box.is_answer_visible(question_index), "Ответ на восьмой вопрос не отображается"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

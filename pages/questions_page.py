from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.questions_locators import QuestionsLocators


class QuestionsBox:
    def __init__(self, driver):
        self.driver = driver


    def get_question_button(self, index):
        return self.driver.find_elements(*QuestionsLocators.QUESTION_BUTTONS)[index]

    def get_answer_panel(self, index):
        return self.driver.find_elements(*QuestionsLocators.ANSWER_PANELS)[index]

    def click_question(self, index):
        element = self.get_question_button(index)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "accordion__button"))
        )
        element.click()

    def is_answer_visible(self, index):
        answer_panel = self.get_answer_panel(index)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(answer_panel)
        )
        return answer_panel.is_displayed()

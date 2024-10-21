from selenium.webdriver.common.by import By
from locators.questions_locators import QuestionsLocators
from pages.base_page import BasePage


class QuestionsBox(BasePage):
    def get_question_button(self, index):
        return self.driver.find_elements(*QuestionsLocators.QUESTION_BUTTONS)[index]

    def get_answer_panel(self, index):
        return self.driver.find_elements(*QuestionsLocators.ANSWER_PANELS)[index]

    def click_question(self, index):
        element = self.get_question_button(index)
        self.scroll_to_element(element)
        self.wait_for_element_to_be_visible((By.CLASS_NAME, "accordion__button"))
        element.click()

    def is_answer_visible(self, index):
        answer_panel = self.get_answer_panel(index)
        self.wait_for_element_to_be_visible(answer_panel)
        return answer_panel.is_displayed()

    def click_confirm_button(self):
        confirm_button = self.find_element(*QuestionsLocators.confirm_button_locator)
        confirm_button.click()
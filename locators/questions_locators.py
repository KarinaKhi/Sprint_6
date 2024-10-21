from selenium.webdriver.common.by import By


class QuestionsLocators:
    QUESTION_BUTTONS = (By.CLASS_NAME, "accordion__button")
    ANSWER_PANELS = (By.CLASS_NAME, "accordion__panel")
    confirm_button_locator = (By.ID, 'rcc-confirm-button')

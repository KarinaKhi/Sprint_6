from conftest import get_random_date
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderPageLocators
from resources.order_data import ORDER_DATA_SET_1, ORDER_DATA_SET_2


class OrderButton:
    def __init__(self, driver):
        self.driver = driver

    def get_order_button_on_top(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_BUTTON_TOP)
        )

    def click_order_button_on_top(self):
        order_button_top = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_TOP)
        )
        order_button_top.click()

    def get_order_button_on_bottom(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        )

    def click_order_button_on_bottom(self):
        bottom_button = self.get_order_button_on_bottom()
        self.driver.execute_script("arguments[0].scrollIntoView();", bottom_button)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        ).click()

    def fill_order_form_start(self, name, surname, address, phone):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

        self.driver.find_element(*OrderPageLocators.METRO_INPUT).click()
        self.driver.find_element(*OrderPageLocators.METRO_STATION_2).click()

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)
        )
        next_button.click()

    def fill_order_form_next(self, comment):
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).click()
        self.select_date()
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY).click()

        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_4).click()

    def select_date(self):
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).click()
        random_date = get_random_date()
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(random_date)

    def click_submit_button(self):
        self.driver.find_element(*OrderPageLocators.SUBMIT_BUTTON).click()

    def click_yes_button(self):
        yes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_YES_BUTTON)
        )
        yes_button.click()

    def click_status_button(self):
        status_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.STATUS_BUTTON)
        )
        status_button.click()

    def click_logo_scooter_button(self):
        logo_scooter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.SCOOTER_LOGO)
        )
        logo_scooter_button.click()

    def click_logo_yandex_button(self):
        logo_yandex_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.YANDEX_LOGO)
        )
        logo_yandex_button.click()

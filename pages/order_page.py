from conftest import get_random_date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_order_button_on_top(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_BUTTON_TOP)
        )

    def click_order_button_on_top(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON_TOP)
        )
        self.click_element(OrderPageLocators.ORDER_BUTTON_TOP)

    def get_order_button_on_bottom(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        )

    def click_order_button_on_bottom(self):
        bottom_button = self.get_order_button_on_bottom()
        self.scroll_to_element(bottom_button)
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    def fill_order_form_start(self, name, surname, address, phone):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

        self.driver.find_element(*OrderPageLocators.METRO_INPUT).click()
        self.driver.find_element(*OrderPageLocators.METRO_STATION_2).click()

    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_order_form_next(self, comment):
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).click()
        self.select_date()
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_4).click()

    def select_date(self):
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).click()
        random_date = get_random_date()
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(random_date)

    def click_submit_button(self):
        self.click_element(OrderPageLocators.SUBMIT_BUTTON)

    def click_yes_button(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    def click_status_button(self):
        self.click_element(OrderPageLocators.STATUS_BUTTON)

    def click_logo_scooter_button(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO)

    def click_logo_yandex_button(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO)

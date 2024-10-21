from locators.order_locators import OrderPageLocators
from pages.order_page import OrderButton
from resources.order_data import ORDER_DATA_SET_1, ORDER_DATA_SET_2, ORDER_DATA_SET_3
from conftest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.constants import YANDEX_URL, BASE_URL


class TestOrderButton:

    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_1, ORDER_DATA_SET_3])
    def test_scooter_order_click_top_button_is_successful(self, driver, open_main_page, order_data):
        order_page = OrderButton(driver)
        order_page.click_order_button_on_top()
        order_page.fill_order_form_start(
            name=order_data['name'],
            phone=order_data['phone'],
            address=order_data['address'],
            surname=order_data['surname']
        )
        order_page.click_next_button()
        order_page.fill_order_form_next(
            comment=order_data['comment']
        )
        order_page.click_submit_button()
        order_page.click_yes_button()
        assert driver.find_element(
            *OrderPageLocators.STATUS_BUTTON).is_displayed(), "Всплывающее окно с подтверждением заказа не появилось"
        order_page.click_status_button()

    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_1, ORDER_DATA_SET_2])
    def test_scooter_order_starts_with_click_on_top_button_then_scooter_logo(self, driver, open_main_page, order_data):
        order_page = OrderButton(driver)
        order_page.click_order_button_on_top()
        order_page.fill_order_form_start(
            name=order_data['name'],
            phone=order_data['phone'],
            address=order_data['address'],
            surname=order_data['surname']
        )
        order_page.click_next_button()
        order_page.fill_order_form_next(comment=order_data['comment'])
        order_page.click_submit_button()
        order_page.click_yes_button()
        order_page.click_status_button()
        order_page.click_logo_scooter_button()
        expected_url = BASE_URL
        assert driver.current_url == expected_url, "Переход на главную страницу не произошел."

    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_1, ORDER_DATA_SET_2])
    def test_scooter_order_starts_with_click_on_top_button_then_yandex_logo(self, driver, open_main_page, order_data):
        order_page = OrderButton(driver)
        order_page.click_order_button_on_top()
        order_page.fill_order_form_start(
            name=order_data['name'],
            phone=order_data['phone'],
            address=order_data['address'],
            surname=order_data['surname']
        )
        order_page.click_next_button()
        order_page.fill_order_form_next(
            comment=order_data['comment']
        )
        order_page.click_submit_button()
        order_page.click_yes_button()
        order_page.click_status_button()
        order_page.click_logo_yandex_button()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.url_contains(YANDEX_URL))
        assert YANDEX_URL in driver.current_url, "Не удалось перейти на главную страницу Дзена."

    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_2, ORDER_DATA_SET_1])
    def test_scooter_order_flow_bottom_button_is_successful(self, driver, order_data, open_main_page):
        order_page = OrderButton(driver)
        order_page.click_order_button_on_bottom()
        order_page.fill_order_form_start(
            name=order_data['name'],
            phone=order_data['phone'],
            address=order_data['address'],
            surname=order_data['surname']
        )
        order_page.click_next_button()
        order_page.fill_order_form_next(
            comment=order_data['comment']
        )
        order_page.click_submit_button()
        order_page.click_yes_button()
        assert driver.find_element(
            *OrderPageLocators.STATUS_BUTTON).is_displayed(), "Всплывающее окно с подтверждением заказа не появилось"
        order_page.click_status_button()

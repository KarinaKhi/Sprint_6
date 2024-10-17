from pages.order_page import OrderButton
from resources.order_data import ORDER_DATA_SET_1, ORDER_DATA_SET_2
from conftest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrderButton:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru')

    def setup_method(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')

    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_1])
    def test_scooter_order_flow_top_button(self, order_data):
        order_page = OrderButton(self.driver)
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

        assert self.driver.find_element(
            *OrderPageLocators.SUCCESS_POPUP).is_displayed(), "Всплывающее окно с подтверждением заказа не появилось"
        order_page.click_status_button()

        order_page.click_logo_scooter_button()
        expected_url = "https://qa-scooter.praktikum-services.ru/"
        assert self.driver.current_url == expected_url, "Переход на главную страницу не произошел."

        order_page.click_logo_yandex_button()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://dzen.ru"))
        assert "https://dzen.ru" in self.driver.current_url, "Не удалось перейти на главную страницу Дзена"

    @pytest.mark.parametrize("order_data", [ORDER_DATA_SET_2])
    def test_scooter_order_flow_bottom_button(self, order_data):
        order_page = OrderButton(self.driver)
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

        assert self.driver.find_element(
            *OrderPageLocators.SUCCESS_POPUP).is_displayed(), "Всплывающее окно с подтверждением заказа не появилось"
        order_page.click_status_button()

        order_page.click_logo_yandex_button()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("https://dzen.ru"))
        assert "https://dzen.ru" in self.driver.current_url, "Не удалось перейти на главную страницу Дзена"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

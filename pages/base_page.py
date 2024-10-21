from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            self.scroll_to_element(element)
            element.click()
        except TimeoutException:
            print(f"Элемент с локатором {locator} не найден или не кликабелен в течение {timeout} секунд.")

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_visible(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(element_or_locator)
            )
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of(element_or_locator)
            )


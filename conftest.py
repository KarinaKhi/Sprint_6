import random
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime, timedelta
from locators.order_locators import OrderPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    return driver


def get_random_date():
    today = datetime.now()
    random_future_date = today + timedelta(days=random.randint(1, 7))  # Дата через 1-7 дней
    return random_future_date.strftime('%d.%m.%Y')

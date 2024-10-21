import random
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime, timedelta
from resources.constants import BASE_URL


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    driver.get(BASE_URL)
    driver.maximize_window()
    return driver


def get_random_date():
    today = datetime.now()
    random_future_date = today + timedelta(days=random.randint(1, 7))
    return random_future_date.strftime('%d.%m.%Y')

import pytest
from selene import browser
from selenium import webdriver

BASE_URL = 'https://demoqa.com'


@pytest.fixture(scope='function', autouse=False)
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = BASE_URL
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options


@pytest.fixture(scope='function', autouse=False)
def practice_form(browser_settings):
    browser.open("/automation-practice-form")

    yield

    browser.quit()

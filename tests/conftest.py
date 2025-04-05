import pytest
import os
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach

BASE_URL = 'https://demoqa.com'


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=False)
def browser_settings():
    browser.config.base_url = BASE_URL
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    url = os.getenv('SELENOID_URL')

    browser.config.driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}/wd/hub",
        options=options)

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

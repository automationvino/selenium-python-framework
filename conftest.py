import pytest
from selenium import webdriver
import os
from datetime import datetime
import sys
from utilities.config_reader import ReadConfig


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://xwctest.services.xerox.com/")
    baseURL = ReadConfig.get_base_url()
    driver.get(baseURL)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup", None)

        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)

            print(f"Screenshot saved: {file_path}")
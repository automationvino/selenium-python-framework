import os
import pytest
from pages.login_page import LoginPage
from utilities.excel_reader import get_test_data
from selenium.webdriver.support import expected_conditions as EC

file_path = os.path.join(os.path.dirname(__file__), "../testdata/login_data.xlsx")
test_data = get_test_data(file_path, "Sheet1")


@pytest.mark.parametrize("username,password,expected", test_data)
def test_login(setup, username, password, expected):

    driver = setup
    login = LoginPage(driver)

    # Perform login
    login.login(username, password)

    # Validation
    if expected.lower() == "pass":
        login.wait.until(EC.url_contains("Admin"))
        assert "Admin" in driver.current_url

    else:
        login.wait.until(EC.url_contains("Login"))
        assert "Login" in driver.current_url
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard_loaded(setup):

    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.login("xpsasdemo1@yopmail.com", "Password01")

    # Wait until Admin page loads
    login.wait.until(EC.url_contains("Admin"))

    print("Current URL:", driver.current_url)

    assert dashboard.is_dashboard_loaded()
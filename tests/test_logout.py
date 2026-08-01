from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_logout(setup):

    driver = setup
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    # Step 1: Login
  
    login.login("xpsasdemo1@yopmail.com", "Password01")

    # Step 2: Logout
    dashboard.logout()

    # Step 3: Wait and validate post-logout URL
    dashboard.wait.until(EC.url_to_be("https://xwctest.services.xerox.com/"))
    assert driver.current_url.lower() == "https://xwctest.services.xerox.com/"
    
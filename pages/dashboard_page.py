from selenium.webdriver.common.by import By
from utilities.logger import get_logger
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.logger = get_logger("DashboardPage")

        self.logout_link = (By.LINK_TEXT, "Logout")

    def is_dashboard_loaded(self):
        return "Admin" in self.driver.current_url

    def logout(self):
        self.logger.info("Clicking Logout")
        self.click(self.logout_link)
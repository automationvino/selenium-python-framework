from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("LoginPage")


        self.login_button = (By.CLASS_NAME, "login")
        self.username = (By.ID, "EmailAddress")
        self.password = (By.ID, "password")
        self.submit_button = (By.ID, "loginSubmitBt")

    def click_login_redirect(self):
        self.logger.info("Clicking Login button")
        self.click(self.login_button)

    
    def login(self, user, pwd):

        self.logger.info("Clicking Login button")
        self.click(self.login_button)

        self.logger.info("Entering username")
        self.type(self.username, user)

        self.logger.info("Clicking first submit")
        self.click(self.submit_button)

        self.logger.info("Waiting for password field")
        self.wait.until(
        EC.visibility_of_element_located(self.password)
    )

        self.logger.info("Entering password")
        self.type(self.password, pwd)

        self.logger.info("Clicking final submit")
        self.click(self.submit_button)

        self.logger.info("Login completed")

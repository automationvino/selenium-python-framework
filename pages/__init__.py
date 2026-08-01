def __init__(self, driver):
    super().__init__(driver)
    self.logger = get_logger(__name__)

    self.login_button = (By.LINK_TEXT, "Login")
    self.username = (By.ID, "EmailAddress")
    self.password = (By.ID, "password")
    self.submit_button = (By.ID, "loginSubmitBt")
    self.login_redirect_btn = (By.CLASS_NAME, "login")
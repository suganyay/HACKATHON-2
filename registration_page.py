from selenium.webdriver.common.by import By
from base_page import BasePage

class RegistrationPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    def register_user(self, first_name, last_name, email, password, confirm_password):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, confirm_password)
        self.click_element(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_element_text(self.SUCCESS_MESSAGE)
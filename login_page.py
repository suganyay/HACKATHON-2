
from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Log in')]")

    def login_user(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
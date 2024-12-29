
from selenium.webdriver.common.by import By
from base_page import BasePage

class LogoutPage(BasePage):
    LOGOUT_BUTTON = (By.LINK_TEXT, "Log out")

    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
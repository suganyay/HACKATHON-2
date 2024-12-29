
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from common import Config


class BasePage:

    def __init__(self, driver):
       self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not found within {timeout} seconds")

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element(locator).text




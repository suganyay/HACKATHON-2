
from selenium.webdriver.common.by import By
from base_page.py import BasePage

class ProductPage(BasePage):
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    PRODUCT_LINK = (By.CSS_SELECTOR, ".product-item h2 a")

    def search_and_select_product(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BUTTON)
        self.click_element(self.PRODUCT_LINK)
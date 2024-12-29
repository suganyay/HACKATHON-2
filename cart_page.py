
from selenium.webdriver.common.by import By
from base_page import BasePage

class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button-4")
    CART_LINK = (By.XPATH, "//a[@class='ico-cart']")

    def add_product_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click_element(self.CART_LINK)
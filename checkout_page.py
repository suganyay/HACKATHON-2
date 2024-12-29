
from selenium.webdriver.common.by import By
from base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    BILLING_CONTINUE_BUTTON = (By.XPATH, "//button[@class='new-address-next-step-button']")
    PAYMENT_CONTINUE_BUTTON = (By.XPATH, "//button[@class='payment-method-next-step-button']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class='confirm-order-next-step-button']")
    ORDER_SUCCESS_MESSAGE = (By.CLASS_NAME, "title")

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)
        self.click_element(self.BILLING_CONTINUE_BUTTON)
        self.click_element(self.PAYMENT_CONTINUE_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)

    def get_order_success_message(self):
        return self.get_element_text(self.ORDER_SUCCESS_MESSAGE)
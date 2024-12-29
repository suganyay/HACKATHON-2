import pytest
from selenium import webdriver
from registration_page import RegistrationPage
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from logout_page import LogoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_page(driver):
    # User Registration
    reg_page = RegistrationPage(driver)
    reg_page.register_user("User", "U", "user123@gmail.com", "user@123", "user@123")
    assert "Your registration completed" in reg_page.get_success_message()

    # User Login
    login_page = LoginPage(driver)
    login_page.login_user("user123gmail.com", "user@123")

    # Product Search & Add to Cart
    product_page = ProductPage(driver)
    product_page.search_and_select_product("Jewelry")

    cart_page = CartPage(driver)
    cart_page.add_product_to_cart()
    cart_page.go_to_cart()

    # Checkout
    checkout_page = CheckoutPage(driver)
    checkout_page.proceed_to_checkout()
    assert "Your order has been successfully processed!" in checkout_page.get_order_success_message()

    # Logout
    logout_page = LogoutPage(driver)
    logout_page.logout()
# test_user_journey.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestUserJourney:

    def test_login_and_purchase(self):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        assert inventory_page.is_inventory_page_displayed()

        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()

        assert cart_page.is_cart_page_displayed()
        cart_page.proceed_to_checkout()

        assert checkout_page.is_checkout_page_displayed()
        checkout_page.enter_checkout_information("John", "Doe", "12345")
        checkout_page.finish_checkout()
        
        assert checkout_page.is_purchase_successful()

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_cart_page_displayed(self):
        return self.is_element_displayed(self.CART_LIST)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

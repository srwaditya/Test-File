from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def is_inventory_page_displayed(self):
        return self.is_element_displayed(self.INVENTORY_CONTAINER)

    def add_to_cart(self, product_name):
        product_locator = (By.XPATH, f"//div[contains(text(), '{product_name}')]/following-sibling::button")
        self.click(product_locator)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)

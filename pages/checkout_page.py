from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ORDER_CONFIRMATION_TEXT = (By.CLASS_NAME, "complete-header")

    def is_checkout_page_displayed(self):
        return self.is_element_displayed(self.CONTINUE_BUTTON)

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME_FIELD, first_name)
        self.enter_text(self.LAST_NAME_FIELD, last_name)
        self.enter_text(self.POSTAL_CODE_FIELD, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def is_purchase_successful(self):
        return self.is_element_displayed(self.ORDER_CONFIRMATION_TEXT)




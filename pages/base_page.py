from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        """Find a single web element"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element not found: {locator}")
            return None

    def find_elements(self, locator):
        """Find multiple web elements"""
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Elements not found: {locator}")
            return []

    def click(self, locator):
        """Click on a web element"""
        element = self.find_element(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        """Enter text into a text field"""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        """Get the text of a web element"""
        element = self.find_element(locator)
        if element:
            return element.text
        return ""

    def is_element_displayed(self, locator):
        """Check if an element is displayed on the page"""
        element = self.find_element(locator)
        return element.is_displayed() if element else False

    def wait_for_element_to_be_clickable(self, locator):
        """Wait for an element to be clickable"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element not clickable: {locator}")
            return None

    def wait_for_element_to_disappear(self, locator):
        """Wait for an element to disappear from the page"""
        try:
            WebDriverWait(self.driver, self.timeout).until_not(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_page_title(self):
        """Get the title of the current page"""
        return self.driver.title

    def go_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)

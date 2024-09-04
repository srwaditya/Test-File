# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()

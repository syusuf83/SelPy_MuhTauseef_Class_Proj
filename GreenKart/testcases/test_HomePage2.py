import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.HomePage import HomePage


@pytest.mark.usefixtures("setup")  # Use the setup fixture
class TestHomePage:

    @pytest.mark.order(1)
    def test_verify_product_title(self):
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the footer to be visible after scrolling
        footer_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='container']//footer"))
        )

        # Extract and print the text of the footer
        footer_text = footer_element.text
        print("Footer Text:", footer_text)
    @pytest.mark.order(1)
    def test_verify_button(self):
        time.sleep(2)

        # Locate all buttons using XPath
        buttons = self.driver.find_elements(By.XPATH, "//div[@class='products']/div/div[3]/button")

        # Click all buttons one by one
        for button in buttons:
            try:
                button.click()
                time.sleep(1)  # Optional: add a delay between clicks if needed
            except Exception as e:
                print(f"Error clicking button: {e}")


import logging
import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.CheckoutPage import CheckoutPage
from POM.HomePage import HomePage


@pytest.mark.usefixtures("setup")  # Use the setup fixture
class TestCheckoutPage:
    @pytest.fixture
    def pre_requirements(self):
        HOME = HomePage(self.driver)

        HOME.get_add_to_cart_product()
        logging.info("clicking on cart button")
        time.sleep(3)
        HOME.get_product_cart_bucket()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HOME.CART_BUCKET_PROCEED_TXT))
        )

        HOME.get_product_cart_bucket_proceed_button()

    @pytest.mark.order(1)
    def test_verify_checkout_page_opening(self, pre_requirements):
        expected_url = "https://rahulshettyacademy.com/seleniumPractise/#/cart"
        current_URL = self.driver.current_url
        assert current_URL in expected_url

    @pytest.mark.order(2)
    def test_verify_product_title(self, pre_requirements):
        CheckOut = CheckoutPage(self.driver)
        actual_title = CheckOut.get_product_Checkout_title()
        expected_title = "Brocolli - 1 Kg"
        assert expected_title in actual_title

    @pytest.mark.order(3)
    def test_verify_product_Qty(self, pre_requirements):
        CheckOut = CheckoutPage(self.driver)
        actual_qty = int(CheckOut.get_product_Checkout_Qty())
        expected_Qty = 1
        assert expected_Qty == actual_qty

    @pytest.mark.order(4)
    def test_verify_product_total(self, pre_requirements):
        CheckOut = CheckoutPage(self.driver)
        actual_qty = CheckOut.get_product_Checkout_Qty()
        actual_price = CheckOut.get_product_Checkout_Price()
        actual_total = int(CheckOut.get_product_Checkout_Total())

        expected_total = int(actual_qty) * int(actual_price)
        assert expected_total == actual_total

    @pytest.mark.order(5)
    def test_verify_place_order_button(self, pre_requirements):
        CheckOut = CheckoutPage(self.driver)
        CheckOut.get_place_order_button_click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("country")
        )

        expected_url = "seleniumPractise/#/cart"
        current_URL = self.driver.current_url
        assert expected_url in current_URL

    @pytest.mark.order(6)
    def test_verify_select_country_Dropdown(self, pre_requirements):
        CheckOut = CheckoutPage(self.driver)
        CheckOut.get_place_order_button_click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("country")
        )
        CheckOut.get_select_country_dropdown()

    @pytest.mark.order(7)
    def test_verify_tos_proceed_button(self, pre_requirements):
        CheckOut = CheckoutPage(self.driver)
        CheckOut.get_place_order_button_click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("country")
        )
        CheckOut.get_select_country_dropdown()

        time.sleep(1)
        CheckOut.get_tos_checkbox_click()
        CheckOut.get_proceed_order_click()
        expected_messge="Thank you, your order has been placed successfully"
        actual_message=CheckOut.get_order_success_msg()
        assert expected_messge in actual_message
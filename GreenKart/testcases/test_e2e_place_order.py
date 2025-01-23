import logging
import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.CheckoutPage import CheckoutPage
from POM.HomePage import HomePage


@pytest.mark.usefixtures("setup")  # Use the setup fixture
class TestE2e:

    @pytest.mark.order(1)
    def test_verify_e2e_place_order(self):
        HOME = HomePage(self.driver)

        HOME.get_add_to_cart_product()
        logging.info("clicking on cart button")
        time.sleep(3)
        HOME.get_product_cart_bucket()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HOME.CART_BUCKET_PROCEED_TXT))
        )

        HOME.get_product_cart_bucket_proceed_button()
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
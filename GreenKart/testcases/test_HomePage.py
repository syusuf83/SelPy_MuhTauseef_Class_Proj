import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from POM.HomePage import HomePage


@pytest.mark.usefixtures("setup")  # Use the setup fixture
class TestHomePage:

    @pytest.mark.order(1)
    def test_verify_product_title(self):
        HOME = HomePage(self.driver)
        product_text = HOME.get_product_title()
        logging.info("getting product name : " + product_text)
        expected_text = "Brocolli - 1 Kg"
        logging.info('expected title : ' + expected_text)

        assert expected_text in product_text
        logging.info("Assertion passed, product title is correct. testcase case is page")

    @pytest.mark.order(2)
    def test_verify_product_price(self):
        HOME = HomePage(self.driver)
        product_price = HOME.get_product_price()
        logging.info("getting product price : " + product_price)
        expected_price = "120"
        logging.info('expected price : ' + expected_price)

        print("expected :" + expected_price)
        print("actual" + product_price)
        assert expected_price in product_price
        logging.info("Assertion passed, product price is correct. testcase case is page")


    @pytest.mark.order(3)
    def test_verify_all_add_to_cart_buttons(self):
        HOME = HomePage(self.driver)
        logging.info("Initializing the object of HomePage class")
        total_product_added_count=HOME.get_add_to_cart_buttons()
        logging.info("clicking on all add to cart buttons with 1 sec delay")

        logging.info("wait for the cart count to be visible")
        footer_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HOME.CART_COUNT))
        )

        assert total_product_added_count==HOME.get_product_cart_count()
        logging.info("assertion passed,all products  added to cart")

    @pytest.mark.order(4)
    def test_verify_cart_bucket(self):
            HOME = HomePage(self.driver)

            HOME.get_add_to_cart_product()
            logging.info("clcikng on cart button")
            time.sleep(1)
            HOME.get_product_cart_bucket()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((HOME.CART_BUCKET_PROCEED_TXT)))

            expected_txt = "PROCEED TO CHECKOUT"
            assert expected_txt == HOME.get_product_cart_bucket_proceed_text()

    @pytest.mark.order(5)
    def test_verify_cart_bucket_proceed_button(self):
        HOME = HomePage(self.driver)

        HOME.get_add_to_cart_product()
        logging.info("clcikng on cart button")
        time.sleep(1)
        HOME.get_product_cart_bucket()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HOME.CART_BUCKET_PROCEED_TXT)))
        HOME.get_product_cart_bucket_proceed_text()

        current_URL = self.driver.current_url
        assert "cart" in current_URL
    @pytest.mark.order(6)
    def test_verify_page_footer_text(self):
        # scroll to bottom
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        logging.info("scrolling down to bottom")
        # wait

        footer_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='container']//footer"))
        )
        logging.info("waiting for the element to be located")
        #extract the text
        footer_element=footer_element.text

        expected_url="© 2019 GreenKart - buy veg and fruits online"
        assert  footer_element in expected_url
        logging.info("assetion executed")


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutPage:
    CHECK_PRODUCT_NAME = (By.XPATH, "//p[@class='product-name']")
    CHECK_PRODUCT_QTY = (By.XPATH, "//div[@class='products']/table/tbody/tr/td[3]/p")
    CHECK_PRODUCT_PRICE = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/p[1]")
    CHECK_PRODUCT_TOTAL= (By.XPATH, "//tbody/tr/td[5]/p[1]")
    CHECK_PLACE_ORDER_BTN= (By.XPATH, "//button[normalize-space()='Place Order']")
    CHECK_COUNTRY_DROPDOWN_SELECT= (By.XPATH, "//div[@class='wrapperTwo']//div//select")
    CHECK_TC_CHECKBOX= (By.XPATH, "//input[@type='checkbox']")
    CHECK_PROCEED_ORDER_BUTTOn= (By.XPATH, "//button[normalize-space()='Proceed']")
    CHECK_ORDER_SUCCESS_MSG= (By.XPATH, "//span[contains(text(),'Thank you, your order has been placed successfully')]")


    def __init__(self, driver):
        self.driver = driver

    def get_product_Checkout_title(self):
        product_text = self.driver.find_element(*self.CHECK_PRODUCT_NAME).text

        return product_text

    def get_product_Checkout_Qty(self):
        product_text = self.driver.find_element(*self.CHECK_PRODUCT_QTY).text

        return product_text


    def get_product_Checkout_Price(self):
        product_text = self.driver.find_element(*self.CHECK_PRODUCT_PRICE).text

        return product_text

    def get_product_Checkout_Total(self):
        product_text = self.driver.find_element(*self.CHECK_PRODUCT_TOTAL).text

        return product_text
    def get_place_order_button_click(self):
        product_place_order_BUTTON = self.driver.find_element(*self.CHECK_PLACE_ORDER_BTN).click()
    def get_select_country_dropdown(self):

        country_dropDOwn=self.driver.find_element(*self.CHECK_COUNTRY_DROPDOWN_SELECT)
        select_country=Select(country_dropDOwn)
        select_country.select_by_value("Germany")

    def get_tos_checkbox_click(self):
         self.driver.find_element(*self.CHECK_TC_CHECKBOX).click()


    def get_proceed_order_click(self):
         self.driver.find_element(*self.CHECK_PROCEED_ORDER_BUTTOn).click()

    def get_order_success_msg(self):
        success_mssg = self.driver.find_element(*self.CHECK_ORDER_SUCCESS_MSG).text

        return success_mssg
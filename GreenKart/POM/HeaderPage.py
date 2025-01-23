from selenium.webdriver.common.by import By


class HeaderPage:
    LOGO = (By.XPATH, "//div[@class='container']//div[@class='container']/div[1]")
    SEARCH = (By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
    OFFER_LINK = (By.XPATH, "//a[normalize-space()='Limited offer - FREE Core Java & QA Resume course']")
    TOP_DEAL_BUTTON = (By.XPATH, "//a[normalize-space()='Top Deals']")
    FLIGHT_BOOKING_BUTTON = (By.XPATH, "//a[normalize-space()='Flight Booking']")
    PRODUCT_TXT = (By.XPATH, "//h4[normalize-space()='Cucumber - 1 Kg']")


    def __init__(self, driver):
        self.driver = driver

    def get_logo_text(self):
        """Geting text"""

        logo_text = self.driver.find_element(*self.LOGO).text
        return logo_text

    def search_product(self, product):
        input_product = self.driver.find_element(*self.SEARCH)
        input_product.clear()
        input_product.send_keys(product)
    def offer_button_click(self):
        input_product = self.driver.find_element(*self.OFFER_LINK).click()
    def topDeal_button_click(self):
       self.driver.find_element(*self.TOP_DEAL_BUTTON).click()
    def Flight_button_click(self):
         self.driver.find_element(*self.FLIGHT_BOOKING_BUTTON).click()

    def get_product_text(self):
       product_text= self.driver.find_element(*self.PRODUCT_TXT).text
       return product_text


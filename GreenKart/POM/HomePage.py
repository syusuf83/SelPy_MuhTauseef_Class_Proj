import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:
    TITLE = (By.XPATH, "//div[@class='products']/div[1]/h4")
    PRICE = (By.XPATH, "//div[@class='products']/div[1]/p")
    ADD_TO_CART_PRODUCT = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//div[@class='products']/div/div[3]/button")
    CART_COUNT = (By.XPATH, "//div[@class='cart-info']/table/tbody/tr[1]/td[3]/strong")
    CART_BUCKET = (By.XPATH, "//a[@class='cart-icon']")
    CART_BUCKET_EMPTY_TXT = (By.XPATH, "(//h2[contains(text(),'You cart is empty!')])[1]")
    CART_BUCKET_PROCEED_TXT = (By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def get_product_title(self):
        product_text = self.driver.find_element(*self.TITLE).text

        return product_text

    def get_product_price(self):
        product_price = self.driver.find_element(*self.PRICE).text
        return product_price

    def get_add_to_cart_product(self):
        self.driver.find_element(*self.ADD_TO_CART_PRODUCT).click()
    def get_add_to_cart_buttons(self):
        #locate all buttons elements
        buttons=self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

        #clicking all buttons one by one via loop
        i=0
        for button in buttons:
            try:

                button.click()
                i+=1
                time.sleep(1)
            except Exception as e:
                print(f"Error in clciking in buttons {e}")
        return str(i)
    def get_product_cart_count(self):
        product_cart_count = self.driver.find_element(*self.CART_COUNT).text
        return product_cart_count

    def get_product_cart_bucket(self):
        try:
            element = self.driver.find_element(*self.CART_BUCKET)
            self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
            ActionChains(self.driver).move_to_element(element).click().perform()
        except Exception as e:
            print(f"Error in clicking button {e}")
            raise
    def get_product_cart_bucket_empty_text(self):
        product_cart_count = self.driver.find_element(*self.CART_BUCKET_EMPTY_TXT).text
        return product_cart_count
    def get_product_cart_bucket_proceed_text(self):
        product_cart_PROCEED_BUTTON = self.driver.find_element(*self.CART_BUCKET_PROCEED_TXT).text
        return product_cart_PROCEED_BUTTON

    def get_product_cart_bucket_proceed_button(self):
        product_cart_PROCEED_BUTTON = self.driver.find_element(*self.CART_BUCKET_PROCEED_TXT).click()

    def get_product_cart_bucket_proceed_text(self):
          self.driver.find_element(*self.CART_BUCKET_PROCEED_TXT).click()

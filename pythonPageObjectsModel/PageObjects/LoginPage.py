# pages/checkout_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    EMAIL_FIELD = (By.XPATH, "//input[@id='userEmail']")
    PASS_FIELD = (By.XPATH, "//input[@id='userPassword']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login']")  # Assuming this is the correct type for the login button

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        """Enter email into the email field."""
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        """Enter password into the password field."""
        password_field = self.driver.find_element(*self.PASS_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        """Complete the login process."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

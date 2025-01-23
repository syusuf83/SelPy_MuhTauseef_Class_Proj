import pytest



from PageObjects.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")  # Use the setup fixture
class TestLoginPage:
    # Define locators as class variables

    def test_verify_login_with_valid_creds(self):
        LOGIN_PAGE = LoginPage(self.driver)

        # Find and interact with elements using defined locators
        #  search_input = self.driver.find_element(By.XPATH, self.SEARCH_FIELD)
        LOGIN_PAGE.enter_email("sufiyan3@gmail.com")
        LOGIN_PAGE.enter_password("123456Aa@")
        LOGIN_PAGE.click_login()

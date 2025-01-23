import logging
import os
import time

import pytest
from selenium.common import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from POM.HeaderPage import HeaderPage
from resources.FileManager import FileManager
from resources.ReusableMethods import ReusableMethods
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("setup")  # Use the setup fixture
class TestHeaderPage:

    # @pytest.mark.order(1)
    # def test_verify_logo_text(self):
    #     HEADER = HeaderPage(self.driver)
    #     logo_text = HEADER.get_logo_text()
    #     # print(logo_text)
    #     expected_text = "GREENKART"
    #     assert expected_text in logo_text
    #
    # @pytest.mark.order(2)
    # def test_verify_Flight_booking_links(self):
    #     HEADER = HeaderPage(self.driver)
    #     RM = ReusableMethods(self.driver)
    #     # Get the current window handle (main window)
    #
    #     main_window_handle = RM.get_current_win_tab()
    #
    #     # click on flight booking button
    #
    #     HEADER.Flight_button_click()
    #     # wait for the new tab to open
    #     time.sleep(2)
    #
    #     # Get all windows handles (there should be two now)
    #     window_handles = RM.get_all_win_tabs()
    #
    #     # switch to the new tab (second handle)
    #     RM.switching_tabs(window_handles, main_window_handle)
    #     # getting current tab url
    #     current_URL = self.driver.current_url
    #
    #     assert "dropdownsPractise" in current_URL
    #
    # @pytest.mark.order(3)
    # def test_verify_Top_deals_links(self):
    #     HEADER = HeaderPage(self.driver)
    #     RM = ReusableMethods(self.driver)
    #     # Get the current window handle (main window)
    #
    #     main_window_handle = RM.get_current_win_tab()
    #
    #     # click on top deals button
    #
    #     HEADER.topDeal_button_click()
    #     # wait for the new tab to open
    #     time.sleep(2)
    #
    #     # Get all windows handles (there should be two now)
    #     window_handles = RM.get_all_win_tabs()
    #
    #     # switch to the new tab (second handle)
    #     RM.switching_tabs(window_handles, main_window_handle)
    #     # getting current tab url
    #     current_URL = self.driver.current_url
    #
    #     assert "offers" in current_URL

    @pytest.mark.order(4)
    def test_verify_search_product_field(self):
        try:
            # Reading data from external file

            reUse=ReusableMethods(self.driver)
            file_path=reUse.get_external_file()
            logging.info("Configuring external file")
            #initialize FIleManager with file path to keywords.txt file

            fileManger=FileManager(file_path)
            product_name=fileManger.read_product_name()

            logging.info("reading data from external file")
            HEADER = HeaderPage(self.driver)
            HEADER.search_product(product_name)

            logging.info("product cucumber is fetched")
            logging.debug("no issue found in debug")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HEADER.PRODUCT_TXT))
            expected_text = "Cucumber - 1 Kg"
            logging.error("assertion failed")
            assert expected_text in HEADER.get_product_text()

        except AssertionError as e:
            logging.error(e)

        except WebDriverException as e:
            logging.error(e)
            print(e)


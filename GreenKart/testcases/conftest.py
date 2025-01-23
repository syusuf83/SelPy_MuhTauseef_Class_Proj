import datetime
import os
import time
import pytest
from selenium import webdriver
import logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Configure logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logs directory if it doesn't exist
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up logging configuration
log_file_path = os.path.join(log_directory, "test_log.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


@pytest.fixture(scope="function")  # scop is class level ye tab execute hoga jab class call hogi

def setup(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://rahulshettyacademy.com/seleniumPractise/"

    driver.get(url)

    logging.info("user is redirected to the url ")
    logging.info("https://rahulshettyacademy.com/seleniumPractise/")
    logging.debug("debug level message")

    driver.implicitly_wait(6)

    request.cls.driver = driver  # cls mean class same like this keyword use hoga jaha ye object use kre gy

 #   yield  # yield keyword lagany se ye code last me exe hoga

#    driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")  # scop is class level ye tab execute hoga jab class call hogi


def setup(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://rahulshettyacademy.com/client//"

    driver.get(url)

    driver.implicitly_wait(6)

    request.cls.driver = driver  # cls mean class same like this keyword use hoga jaha ye object use kre gy

#  yield  # yield keyword lagany se ye code last me exe hoga
#  driver.close()

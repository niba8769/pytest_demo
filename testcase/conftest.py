import pytest
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    exe = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=exe)
    driver.implicitly_wait(10)
    return driver


# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

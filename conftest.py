import pytest

import time
from time import sleep

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def set_driver_chrome():
    driver_chrome = Chrome("chromedriver.exe")
    return driver_chrome

@pytest.fixture()
def set_driver_firefox():
    driver_firefox = firefox("geckodriver.exe")
    return driver_firefox

@pytest.fixture()
def set_driver_edge():
    driver_edge = edge("geckodriver.exe")
    return driver_edge
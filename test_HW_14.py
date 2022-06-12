import time
from time import sleep

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

def test_authorisation_chrome(set_driver_chrome):
    try:
        user_email = 'OlenaL'
        user_password = 'VTfRkcJVNi'
        set_driver_chrome.get('http://loveread.ec/index.php')
        email_locator = '//*[@id="login"]'
        time.sleep(5)
        email_element = set_driver_chrome.find_element(By.XPATH, email_locator)
        email_element.send_keys(user_email)
        time.sleep(5)
        password_locator = '//*[@id="password"]'
        password_element = set_driver_chrome.find_element(By.XPATH, password_locator)
        password_element.send_keys(user_password)
        time.sleep(5)
        login_button_locator = '//*[contains(@name, "submit_enter")]'
        login_button_element = set_driver_chrome.find_element(By.XPATH, login_button_locator)
        login_button_element.click()
        time.sleep(5)
        our_title = set_driver_chrome.title
        assert our_title == 'LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации', f'\nwrong title\nActual: {our_title}\nExpected: LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации'
        print('f{our_title}')
    except:
        driver_chrome.quit()

def test_authorisation_firefox(set_driver_firefox):
    try:
        user_email = 'OlenaL'
        user_password = 'VTfRkcJVNi'
        set_driver_firefox.get('http://loveread.ec/index.php')
        email_locator = '//*[@id="login"]'
        time.sleep(5)
        email_element = set_driver_firefox.find_element(By.XPATH, email_locator)
        email_element.send_keys(user_email)
        time.sleep(5)
        password_locator = '//*[@id="password"]'
        password_element = set_driver_firefox.find_element(By.XPATH, password_locator)
        password_element.send_keys(user_password)
        time.sleep(5)
        login_button_locator = '//*[contains(@name, "submit_enter")]'
        login_button_element = set_driver_firefox.find_element(By.XPATH, login_button_locator)
        login_button_element.click()
        time.sleep(5)
        our_title = set_driver_firefox.title
        assert our_title == 'LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации', f'\nwrong title\nActual: {our_title}\nExpected: LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации'
        print('f{our_title}')
    except:
        driver_chrome.quit()

def test_authorisation_edge(set_driver_edge):
    try:
        user_email = 'OlenaL'
        user_password = 'VTfRkcJVNi'
        set_driver_edge.get('http://loveread.ec/index.php')
        email_locator = '//*[@id="login"]'
        time.sleep(5)
        email_element = set_driver_edge.find_element(By.XPATH, email_locator)
        email_element.send_keys(user_email)
        time.sleep(5)
        password_locator = '//*[@id="password"]'
        password_element = set_driver_edge.find_element(By.XPATH, password_locator)
        password_element.send_keys(user_password)
        time.sleep(5)
        login_button_locator = '//*[contains(@name, "submit_enter")]'
        login_button_element = set_driver_edge.find_element(By.XPATH, login_button_locator)
        login_button_element.click()
        time.sleep(5)
        our_title = set_driver_edge.title
        assert our_title == 'LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации', f'\nwrong title\nActual: {our_title}\nExpected: LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации'
        print('f{our_title}')
    except:
        driver_chrome.quit()
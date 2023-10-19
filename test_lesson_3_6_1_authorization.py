import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    time.sleep(30)
    browser.quit()


@pytest.mark.parametrize('my_login, my_pass', [('****', '****')])
def test_authorization(browser, my_login, my_pass):
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link)
    button_entry = browser.find_element(By.ID, 'ember33')
    button_entry.click()
    field_email = browser.find_element(By.ID, 'id_login_email')
    field_email.send_keys(my_login)
    field_pass = browser.find_element(By.ID, 'id_login_password')
    field_pass.send_keys(my_pass)
    button = browser.find_element(By.CLASS_NAME, 'button_with-loader')
    button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()
try:
    browser.get(link)

    field_first_name = browser.find_element(By.NAME, 'firstname')
    field_first_name.send_keys('my_name')

    field_second_name = browser.find_element(By.NAME, 'lastname')
    field_second_name.send_keys('my_surname')

    field_email = browser.find_element(By.NAME, 'email')
    field_email.send_keys('email@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)

    button_file = browser.find_element(By.ID, 'file')
    button_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(40)
    browser.quit()

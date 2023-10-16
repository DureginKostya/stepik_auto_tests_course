from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_el = x_element.text
    y = calc(x_el)
    field_result = browser.find_element(By.CSS_SELECTOR, '#answer')
    field_result.send_keys(y)
    checkbox_click = browser.find_element(By.CSS_SELECTOR, '#robotCheckBox')
    checkbox_click.click()
    radiobutton_click = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton_click.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(30)
    browser.quit()

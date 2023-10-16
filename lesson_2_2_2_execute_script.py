from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_el = x_element.text
    y = calc(x_el)

    field_result = browser.find_element(By.ID, "answer")


    field_result.send_keys(y)

    checkbox_click = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_click)
    checkbox_click.click()

    radiobutton_click = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_click)
    radiobutton_click.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(30)
    browser.quit()

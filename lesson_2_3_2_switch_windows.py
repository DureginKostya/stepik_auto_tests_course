from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
try:
    browser.get(link)

    button_fly = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_fly.click()

    current_wnd = browser.window_handles[0]
    next_wnd = browser.window_handles[1]

    browser.switch_to.window(next_wnd)

    time.sleep(1)

    x_element = browser.find_element(By.ID, 'input_value')
    x_el = x_element.text
    y = calc(x_el)

    field_result = browser.find_element(By.ID, 'answer')
    field_result.send_keys(y)

    button_new_window = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_new_window.click()


finally:
    time.sleep(30)
    browser.quit()

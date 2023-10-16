import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_el = x_element.text
    y = calc(x_el)

    field_result = browser.find_element(By.CSS_SELECTOR, '#answer')
    field_result.send_keys(y)

    button_result = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    )
    button_result.click()
finally:
    time.sleep(30)
    browser.quit()

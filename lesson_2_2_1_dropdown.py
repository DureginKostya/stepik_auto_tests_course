from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
try:
    browser.get(link)
    number_one = (browser.find_element(By.ID, 'num1')).text
    number_two = (browser.find_element(By.ID, 'num2')).text
    sum_numbers = str(int(number_one) + int(number_two))
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(sum_numbers)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(30)
    browser.quit()

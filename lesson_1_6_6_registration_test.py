from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    required_field_one = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
    required_field_one.send_keys('One')
    required_field_two = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
    required_field_two.send_keys('Two')
    required_field_three = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
    required_field_three.send_keys('Three')

    # elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    # for element in elements:
    #     element.send_keys('Hello')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

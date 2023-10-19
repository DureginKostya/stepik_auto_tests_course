import time
import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RESULT = []


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    # browser.implicitly_wait(10)
    yield browser
    time.sleep(5)
    browser.quit()


class TestStepik:

    @pytest.mark.parametrize('link, my_login, my_pass, answer',
                             [('https://stepik.org/lesson/236895/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236896/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236897/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236898/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236899/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236903/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236904/step/1', '****', '****', 'Correct!'),
                              ('https://stepik.org/lesson/236905/step/1', '****', '****', 'Correct!')])
    def test_authorization(self, browser, link, my_login, my_pass, answer):
        browser.get(link)
        button_entry = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.ID, 'ember33'))
        )
        button_entry.click()

        field_email = browser.find_element(By.ID, 'id_login_email')
        field_email.send_keys(my_login)

        field_pass = browser.find_element(By.ID, 'id_login_password')
        field_pass.send_keys(my_pass)

        button = browser.find_element(By.CLASS_NAME, 'button_with-loader')
        button.click()

        time.sleep(10)

        textarea = browser.find_element(By.CLASS_NAME, 'ember-text-area')
        textarea.send_keys(math.log(int(time.time())))

        button_submit = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        )
        button_submit.click()

        field_feedback = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        )

        message_feedback = field_feedback.text
        assert message_feedback == answer, RESULT.append(message_feedback.strip())

    def test_write_answer(self):
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(' '.join(RESULT))


if __name__ == '__main__':
    TestStepik()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestSite(unittest.TestCase):

    @staticmethod
    def _get_answer(link):
        browser = webdriver.Chrome()
        browser.get(link)
        required_field_one = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        required_field_one.send_keys('One')
        required_field_two = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        required_field_two.send_keys('Two')
        required_field_three = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
        required_field_three.send_keys('Three')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        time.sleep(30)
        browser.quit()
        return welcome_text

    def test_site_first(self):
        result = self._get_answer('http://suninjuly.github.io/registration1.html')
        self.assertTrue("Congratulations! You have successfully registered!" == result)

    def test_site_second(self):
        result = self._get_answer('http://suninjuly.github.io/registration2.html')
        self.assertTrue("Congratulations! You have successfully registered!" == result)


if __name__ == "__main__":
    unittest.main()

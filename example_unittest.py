import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_registration_1(self):
        driver = webdriver.Firefox()
        driver.get("http://suninjuly.github.io/registration1.html")
        driver.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input").send_keys("Ivan")
        driver.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input").send_keys("Petrov")
        driver.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input").send_keys("aaa@net.ru")
        driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)
        driver.quit()
        #успешный тест

    def test_registration_2(self):
        driver = webdriver.Firefox()
        driver.get("http://suninjuly.github.io/registration2.html")
        driver.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input").send_keys("Ivan")
        driver.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input").send_keys("Petrov")
        driver.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input").send_keys("aaa@net.ru")
        driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text_elt.text)
        driver.quit()
        #тест с ошибкой

if __name__ == "__main__":
    unittest.main()
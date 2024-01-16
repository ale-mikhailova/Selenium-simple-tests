import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser(scope="class"):
    browser = webdriver.Firefox()
    yield browser
    browser.quit()

class TestParametrization():
    @pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", \
                                        "https://stepik.org/lesson/236896/step/1", \
                                        "https://stepik.org/lesson/236897/step/1", \
                                        "https://stepik.org/lesson/236898/step/1", \
                                        "https://stepik.org/lesson/236899/step/1", \
                                        "https://stepik.org/lesson/236903/step/1", \
                                        "https://stepik.org/lesson/236904/step/1", \
                                        "https://stepik.org/lesson/236905/step/1"])
    def test_authorization(self, browser, links): 
        link = f"{links}"
        browser.get(link)
        WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, "ember33"))).click()
        WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, "id_login_email"))).send_keys("your_mail")
        WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, "id_login_password"))).send_keys("your_password")
        browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
        text_area = WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        text_area.send_keys(str(math.log(int(time.time()))))
        browser.implicitly_wait(5)
        WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
        browser.implicitly_wait(5)
        text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        assert text == "Correct!", f"{text}"
        

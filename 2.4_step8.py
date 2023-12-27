import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #ожидание нужного теста на странице
driver.find_element(By.TAG_NAME, "button").click()

elem = driver.find_element(By.ID, "input_value").text
input_answer = driver.find_element(By.ID, "answer")
input_answer.send_keys(str(math.log(abs(12*math.sin(int(elem ))))))

driver.find_element(By.ID, "solve").click()
time.sleep(1)
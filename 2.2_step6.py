import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://SunInJuly.github.io/execute_script.html")
elem = driver.find_element(By.ID, "input_value").text
input_answer = driver.find_element(By.ID, "answer")
input_answer.send_keys(str(math.log(abs(12*math.sin(int(elem ))))))

driver.execute_script("window.scrollBy(0, 100);") #работа с js-скриптом

driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.CSS_SELECTOR, "[value='robots']").click()
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)

driver.quit()
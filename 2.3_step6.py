import time
import math

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://suninjuly.github.io/redirect_accept.html")
driver.find_element(By.TAG_NAME, "button").click()
new_window = driver.window_handles[1]
driver.switch_to.window(new_window) #переход на новую вкладку
time.sleep(1)

elem = driver.find_element(By.ID, "input_value").text
input_answer = driver.find_element(By.ID, "answer")
input_answer.send_keys(str(math.log(abs(12*math.sin(int(elem ))))))
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(5)

driver.quit()
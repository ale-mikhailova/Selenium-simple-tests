from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x_element)
	
    time.sleep(1)
	
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
	
    time.sleep(1)
	
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
	
    time.sleep(1)
	
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click()

finally:
    time.sleep(5)
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value").text
    print(x_element)
    y = calc(x_element)
	
    time.sleep(2)
	
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
	
    time.sleep(2)
	
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
	
    time.sleep(2)
	
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn") 
    button.click()

finally:
    time.sleep(3)
    browser.quit()
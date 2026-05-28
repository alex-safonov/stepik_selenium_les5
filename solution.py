from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    
    time.sleep(1)
    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    #option1 = browser.find_element(By.ID, "[value='robotCheckbox']")
    #option1.click()
    
    time.sleep(1)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    
    time.sleep(1)
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    
    time.sleep(1)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    

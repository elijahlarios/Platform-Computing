from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()

driver.get("http://localhost:3000")

title = driver.title

driver.implicitly_wait(0.5) 

# about_header = driver.find_element(by=By.CSS_SELECTOR, value='.main-header')
about_header = driver.find_element(by=By.ID, value="abt")

# text_box.send_keys("Selenium")
time.sleep(1)
about_header.clear()
time.sleep(1)
about_header.send_keys("Selenium")
time.sleep(2)

print("done")
driver.quit()
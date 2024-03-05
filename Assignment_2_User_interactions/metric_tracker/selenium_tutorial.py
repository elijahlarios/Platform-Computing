from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("http://localhost:3000")

title = driver.title

driver.implicitly_wait(0.5)

# text_box = driver.find_element(by = By.NAME, value="About Me")
github_button = driver.find_element(by=By.CSS_SELECTOR, value='.main-header')

# text_box.send_keys("Selenium")
github_button.send_keys("Selenium")

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

driver.quit()
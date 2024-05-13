from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from elijah_user import userAction
from User28 import userAction
driver = webdriver.Chrome()

driver.get("https://platform-computing.vercel.app/assignment1.html")
userAction(driver)
driver.quit()
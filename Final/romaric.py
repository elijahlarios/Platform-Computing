import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

def create_unique_user():
    urls = ["https://platform-computing.vercel.app/assignment1.html"]
    webdriver_path = '/Users/romaricallahramadji/Documents/Platform_Computing/Assignment_2_User_Interactions/Metric_tracker/chromedriver'
    
    total_presence_time = 0
    
    driver = webdriver.Chrome()
    
    for url in urls:
        start_time = time.time()
        driver.get(url)
        time.sleep(random.uniform(5, 10))  # Random sleep to simulate reading time
        
        # Check for images on the page
        images = driver.find_elements(By.TAG_NAME, "img")
        if not images:  # If there are no images, reduce the base presence time
            print(f"No images found on {url}. Reducing presence time.")
            base_presence_time = 5  # Reduced base presence time
        else:
            base_presence_time = 10  # Default base presence time if images are found
        
        time.sleep(base_presence_time)  # Sleep for base presence time
        
        # ...[rest of your code for scrolling, clicking links, and interacting with forms]

        page_presence_time = time.time() - start_time
        total_presence_time += page_presence_time
        print(f"Presence time on {url}: {page_presence_time:.2f} seconds")
        
    print(f"Total presence time across all pages: {total_presence_time:.2f} seconds")
    
    # Close the browser at the end of the session
    driver.quit()

create_unique_user()
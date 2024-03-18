from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Edge()

driver.get("http://localhost:3000")

metrics = []
SCROLL_HEIGHT = "return document.body.scrollHeight"
CURRENT_SCROLL = "return window.pageYOffset"
ELEM_ID = "abt"
CLICK_LISTENER = f"var clicks = 1; var element = document.getElementById('{ELEM_ID}');element.onclick=function() {{element.textContent='Clicks: ' + clicks; clicks++;}}"

click_listener = driver.execute_script(CLICK_LISTENER)    
about_header = driver.find_element(by=By.ID, value=ELEM_ID)
initial_header = about_header.text

clicks = 0
title = driver.title
p_elems = []
start_time = time.time()
current_time = 0
presence_time= 0
max_current_scroll = 0
while presence_time <= 50:
    # get time user is active
    current_time = round(time.time(), 2)
    presence_time = abs(round(current_time - start_time, 2))
    print(f"Presence time: {presence_time}")

    # track scrolling
    scroll_height = driver.execute_script(SCROLL_HEIGHT)
    current_scroll = driver.execute_script(CURRENT_SCROLL)
    print(f"Current Scroll Pos: {current_scroll}/{scroll_height} pixels")
    if current_scroll > max_current_scroll:
        max_current_scroll = current_scroll
    time.sleep(2)

    # track clicks (utilizes JS function outside of loop)
    if about_header.text != "About Me":
        print(about_header.text)
        # click_amt = about_header.text[-1]
        # clicks = int(click_amt)
        click_amt = ''.join(click for click in about_header.text if click.isdigit())
        clicks = int(click_amt)

    else: 
        print("Clicks: 0")

paragraphs = driver.find_elements(by=By.CLASS_NAME, value='main-body')
for p in paragraphs:
    p_elems.append(p.text)

driver.quit()

# when presence time > 50: append all saved items to CSV
data = {
    'presence time': presence_time,
    'pixels scrolled': max_current_scroll,
    'clicks': clicks,
    'title': title,
    'header': initial_header,
    'paragraph contents': [p_elems]
}
df = pd.DataFrame(data)
df.to_csv('metrics.csv', index=False)

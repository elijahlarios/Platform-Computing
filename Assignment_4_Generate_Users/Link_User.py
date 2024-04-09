import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from sys import argv

def adjust_time(links) -> None:
    if links:
        time.sleep(len(links) * 10)

def determine_time(url: str) -> None:
    driver = Edge()

    # keyword test
    driver.get(url)
    time.sleep(2) # allow page load
    start_time: float = time.time()
    presence_time: float = 0

    links = driver.find_elements(By.TAG_NAME, 'a')
    adjust_time(links)
    current_time: float = round(time.time(), 2)
    presence_time = abs(round(current_time - start_time, 2))

    print(f"Presence time on {url}: {presence_time}s")
    driver.quit()


def main() -> None:
    URL_WITH_LINK: str = 'https://platform-computing.vercel.app/assignment1.html'
    URL_WITHOUT_LINK: str = 'https://tunit.cloud/'

    if argv[1] == str(0):
        determine_time(URL_WITH_LINK)
    else:
        determine_time(URL_WITHOUT_LINK)




if __name__ == '__main__':
    main()
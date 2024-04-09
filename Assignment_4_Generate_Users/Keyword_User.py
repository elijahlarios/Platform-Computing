import time
from selenium.webdriver import Edge
from sys import argv

def adjust_time(search_content: str, keyword: str) -> None:
    if keyword.lower() in search_content.lower():
        time.sleep(10) # increase presence_time by 10s

def determine_time(url: str, keyword: str) -> None:
    driver = Edge()

    # keyword test
    driver.get(url)
    time.sleep(2) # allow page load
    start_time: float = time.time()
    presence_time: float = 0
    content: str = driver.page_source


    adjust_time(content, keyword)
    current_time: float = round(time.time(), 2)
    presence_time = abs(round(current_time - start_time, 2))

    print(f"Presence time on {url}: {presence_time}s")
    driver.quit()


def main() -> None:
    KEYWORD: str = 'Lucky'
    URL_WITH_KEYWORD: str = 'http://google.com'
    URL_WITHOUT_KEYWORD: str = 'http://apple.com'

    if argv[1] == str(0):
        determine_time(URL_WITH_KEYWORD, KEYWORD)
    else:
        determine_time(URL_WITHOUT_KEYWORD, KEYWORD)




if __name__ == '__main__':
    main()
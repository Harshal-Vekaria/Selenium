from selenium.webdriver import Chrome
from time import sleep

# http://127.0.0.1:9515/session
browser = Chrome("/Users/sandeep/Desktop/training/_selenium/training/chromedriver")

# http://127.0.0.1:9515/session/bbca4c78371e97b5d07f7a002f8356ec/url
browser.get("https://demowebshop.tricentis.com/")
sleep(2)
browser.maximize_window()
sleep(2)
browser.minimize_window()
sleep(2)
browser.maximize_window()
sleep(2)

# prints the current url of the webpage
url = browser.current_url

# title returns the current title of the webpage
browser_title = browser.title

# http://127.0.0.1:9515/session/02316b754f85195115c5cb89bc86b96a/window
browser.quit()
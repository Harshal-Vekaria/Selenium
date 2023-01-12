from selenium.webdriver import Chrome
from time import sleep

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/demo.html")
sleep(2)
# ====================================================================================================================

boxes = driver.find_elements_by_name("fname")
words = ["apple", "google", "yahoo", "gmail", "facebook", "instagram", "watsapp", "twitter", 'walmart']

for box, word in zip(boxes, words):
    box.send_keys(word)
    sleep(1)

#====================================================================================================================
# close browser session
sleep(2)
driver.close()

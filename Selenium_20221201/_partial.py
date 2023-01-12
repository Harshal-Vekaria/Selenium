from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver")

driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/demo.html")
sleep(2)

driver.find_element_by_partial_link_text("Inbox").click()
        

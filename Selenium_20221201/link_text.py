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

# solution-1
# links = driver.find_elements_by_tag_name("a")

# solution-2
links = driver.find_elements_by_xpath("//a")

for link in links:
    print(link.text)
    sleep(1)

#====================================================================================================================
# close browser session
sleep(2)
driver.close()

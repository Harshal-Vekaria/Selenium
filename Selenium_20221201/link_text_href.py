from selenium.webdriver import Chrome
from time import sleep

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("https://www.python.org/")
sleep(5)
# ====================================================================================================================
links = driver.find_elements_by_xpath("//a")
items = [ ]
for link in links:
    link_text = link.text.strip()
    if "Python" in link_text:
        # append a tuple of linktext and value of "href" attribute
        items.append((link_text, link.get_attribute('href')))
        sleep(0.2)

#====================================================================================================================
# close browser session
sleep(2)
driver.close()

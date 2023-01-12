from selenium.webdriver import Chrome
from time import sleep

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("https://demowebshop.tricentis.com/books")
sleep(5)
# ====================================================================================================================

images = driver.find_elements_by_xpath("//img")

for image in images:
    print(image.get_attribute("title"))

#====================================================================================================================
# close browser session
sleep(2)
driver.close()

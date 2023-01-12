from selenium.webdriver import Chrome
from time import sleep

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/demo.html")
sleep(5)
# ====================================================================================================================
# find all images
images = driver.find_elements_by_xpath("//img")

# find all links
links = driver.find_elements_by_xpath("//a")

# find all textboxes
boxes = driver.find_elements_by_xpath("//input[@type='text']")

# find all radio buttons
radios = driver.find_elements_by_xpath("//input[@type='radio']")

# find all checkboxes
c_boxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(f"Total No. of images: {len(images)}")
print(f"Total No. of links: {len(links)}")
print(f"Total No. of textboxes: {len(boxes)}")
print(f"Total No. of radio buttons: {len(radios)}")
print(f"Total No. of checkboxes: {len(c_boxes)}")

#====================================================================================================================
# close browser session
sleep(2)
driver.close()








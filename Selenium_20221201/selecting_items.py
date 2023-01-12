from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/demo.html")
sleep(5)
# ====================================================================================================================

cars_list_box = driver.find_element_by_id("standard_cars")

s = Select(cars_list_box)

s.select_by_visible_text("Mercedes")
sleep(2)
s.select_by_visible_text("Audi")
sleep(2)
s.select_by_visible_text("Toyota")
sleep(2)

s.select_by_index(6)
sleep(2)
s.select_by_index(1)
sleep(2)
s.select_by_index(11)
sleep(2)

s.select_by_value("for")
sleep(2)
s.select_by_value("hda")
sleep(2)
s.select_by_value("nin")
sleep(2)
#====================================================================================================================
# close browser session
sleep(2)
driver.close()








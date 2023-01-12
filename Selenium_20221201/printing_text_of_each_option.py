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

# options is a property and it retuns a list of all the options present in the list box
# each item in the list is a webelement. (options property returns list of all the option tags)
# each option tag is a webelement
# in order to get the text of any webelement, we have to use a property .text
all_options = s.options

# using normal method of building a list
items = [ ]
for item in all_options:
    items.append(item.text)

# using list comprehension
_items = [ item.text for item in all_options ]

#====================================================================================================================
# close browser session
sleep(2)
driver.close()


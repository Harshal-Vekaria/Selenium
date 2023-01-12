from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
from csv import reader
from re import findall
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/loading.html")
#====================================================================================================================

# driver.find_element_by_xpath("//button[text()='Click Me']").click()

# dynamic or webdriver wait or explicit wait
w = WebDriverWait(driver, 20)
#v = visibility_of_element_located(("id", "fname"))
# 1. visibility_of_element_located class takes care of two things
# 1. waits until the element is loaded in the DOM or in HTML
# 2. waits until the element is visible on the webpage
# until method raises timeoutexception if the above conditions are not met within max timeout 
# period
v = visibility_of_element_located(("id", "fname"))
# before entering fname plese wait for a webelement where the value of "id" attribute is "fname"
w.until(v)

                                  # print("DONE!!!!")

driver.find_element_by_id("fname").send_keys("hello world")






























#====================================================================================================================
# close browser session
#sleep(2)
#driver.close()


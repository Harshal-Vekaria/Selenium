from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
from csv import reader
from re import findall
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, title_is

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/loading.html")
#====================================================================================================================

# driver.find_element_by_xpath("//button[text()='Click Me']").click()


class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        # calling parent class __call__ method
        # reusing the original functionality given by perent class
        # (checking if the elemetn is loaded in the DOM and visible on the webpage)
        result = super().__call__(driver)
        # Extra functionality in child class __call__ method
        if isinstance(result, WebElement):
            # checking if the element is enabled or not
            # if the element is enabled, is_enabled function returns boolean True
            # else it will return False
            return  result.is_enabled()
        return False

# dynamic or webdriver wait or explicit wait
w = WebDriverWait(driver, 20)
#v = visibility_of_element_located(("id", "fname"))
# 1. visibility_of_element_located class takes care of two things
# 1. waits until the element is loaded in the DOM or in HTML
# 2. waits until the element is visible on the webpage
# until method raises timeoutexception if the above conditions are not met within max timeout 
# period

#t = title_is("Demo Web Shop")
#w.until(t)

v = _visibility_of_element_located(("id", "fname"))
# before entering fname plese wait for a webelement where the value of "id" attribute is "fname"
w.until(v)

driver.find_element_by_id("fname").send_keys("hello world")






























#====================================================================================================================
# close browser session
#sleep(2)
#driver.close()


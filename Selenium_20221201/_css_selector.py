from selenium.webdriver import Chrome
from time import sleep

# CSS Selectors are used to select webelements on the webapge from stylesheet
# we can use CSS selectors in selenium to help selenium identity element on the webpage.
# General Syntax of the CSS selector is 

# HTMLTAG[attribute_value='attribute_value']

driver = Chrome("./chromedriver")
driver.get("https://demowebshop.tricentis.com/")
sleep(5)

driver.find_element_by_css_selector("a[class='ico-register']").click()
sleep(2)

#input[value='M']
#input[id='gender-male']
#input[name='Gender']
#input[type='radio']
driver.find_element_by_css_selector("input[value='M']").click()

#input[id='FirstName']
#input[name='FirstName']
driver.find_element_by_css_selector("input[id='FirstName']").send_keys("hello")
sleep(2)

# input[name='LastName']
# input[id='LastName']
driver.find_element_by_css_selector("input[id='LastName']").send_keys("world")
sleep(2)

# input[id='Email']
# input[name='Email']
driver.find_element_by_css_selector("input[id='Email']").send_keys("hello.world@company.com")
sleep(2)

# input[name='Password']
# input[id='Password']

driver.find_element_by_css_selector("input[name='Password']").send_keys("Password123")
sleep(2)

driver.find_element_by_css_selector("input[id='ConfirmPassword']").send_keys("Password123")
sleep(2)
# input[id='register-button']
# input[name='register-button']
# input[value='Register']
driver.find_element_by_css_selector("input[id='register-button']").click()

















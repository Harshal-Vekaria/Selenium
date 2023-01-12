from time import sleep
from selenium.webdriver import Chrome

# Creates a new Chrome browser session
driver = Chrome("/Users/sandeep/Desktop/training/_selenium/training/chromedriver")

# Navigate to demowebshop
driver.get("https://demowebshop.tricentis.com/")

# Maximizes the browser window
driver.maximize_window()

# driver.find_element_by_class_name("ico-register").click()
driver.find_element_by_link_text("register").click()
sleep(2)
driver.find_element_by_id("gender-male").click()
driver.find_element_by_id("FirstName").send_keys("hello")
driver.find_element_by_name("LastName").send_keys("world")
driver.find_element_by_id("Email").send_keys("hello.world@compnay.com")
driver.find_element_by_id("Password").send_keys("Password123")
driver.find_element_by_id("ConfirmPassword").send_keys("Password123")
driver.find_element_by_name("register-button").click()
driver.quit()

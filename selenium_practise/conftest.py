from pytest import fixture
from selenium.webdriver import Chrome
from time import sleep

# fixture is a callable which is used to pass data to the test methods
# we can access the data that is returned by the fixture by referring to the name of the fixture in test method or functions
# the lines of code before yield keyword will be executed once per test method and the lines of code after yield keyword
# will be executed once after every test method

@fixture
def setup_tear_down():
    driver = Chrome("./chromedriver.exe")
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    sleep(4)
    yield driver
    driver.close()



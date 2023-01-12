from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def _wait(func):
    def wrapper(*args, **kwargs):   # args = (self, ("id", "gender-male") )
        instance = args[0]
        locator = args[1]
        print(f"waiting for element {locator}")
        w = WebDriverWait(instance.driver, 20)
        v = _visibility_of_element_located(locator)
        w.until(v)
        # actual func is executed here (click_element, enter_text)
        return func(*args, **kwargs)
    return wrapper

class SeleniumWrapper:
    def __init__(self, obj_instance):
        self.driver = obj_instance
    
    @_wait
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    
    @_wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()   

    @_wait
    def select_item(self, locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visibile_text(item)
        else:
            s.select_by_index(item)


















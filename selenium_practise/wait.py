from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement


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
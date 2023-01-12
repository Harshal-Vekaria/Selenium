from selenium.webdriver.support.select import Select
from wait import _wait


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
            s.select_by_visible_text(item)
        else:
            s.select_by_index(item)



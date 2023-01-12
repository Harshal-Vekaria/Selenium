from lib import SeleniumWrapper

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_register(self):
        sw = SeleniumWrapper(self.driver)
        sw.click_element(("link text", "Register"))

    def click_login(self):
        sw = SeleniumWrapper(self.driver)
        sw.click_element(("link text", "Log in"))

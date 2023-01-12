from lib import SeleniumWrapper
from xl_lib import read_locators

class LoginPage(SeleniumWrapper):

    login_page_objects = read_locators("loginpage")

    def __init__(self, driver):
        super().__init__(driver)

    # login function
    def login(self, email, password):
        # create object instance to seleniumwrapper class
        sw = SeleniumWrapper(self.driver)
        
        # enter email 
        sw.enter_text(LoginPage.login_page_objects['txt_email'], value=email)
        
        # enter password
        sw.enter_text(LoginPage.login_page_objects['txt_password'], value=password)
        
        # click login
        sw.click_element(LoginPage.login_page_objects['btn_login'])











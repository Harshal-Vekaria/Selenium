from lib import SeleniumWrapper
from xl_lib import read_locators

class RegistrationPage(SeleniumWrapper):
    
    registration_page_objects = read_locators("registrationpage")

    def __init__(self, driver):
        super().__init__(driver)

    def register_user(self, gender, fname, lname, email, password, confirmpassword):

        # select gender
        if gender == "Male":
            self.click_element(self.__class__.registration_page_objects['rdo_male'])
        else:
            self.click_element(self.__class__.registration_page_objects['rdo_female'])
        
        # enter firstname 
        self.enter_text(self.__class__.registration_page_objects["txt_fname"], value=fname)
        
        # enter lastname
        self.enter_text(self.__class__.registration_page_objects['txt_lname'], value=lname)

        # enter email
        self.enter_text(RegistrationPage.registration_page_objects['txt_email'], value=email)
        
        # enter password
        self.enter_text(self.__class__.registration_page_objects['txt_password'], value=password)
    
        # enter confirm password
        self.enter_text(self.__class__.registration_page_objects['txt_confirm_password'], value=confirmpassword)

        # click register button
        self.click_element((self.__class__.registration_page_objects['btn_register']))





        

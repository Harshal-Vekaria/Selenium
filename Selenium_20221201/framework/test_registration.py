from lib import SeleniumWrapper
from pytest import mark
from registrationpage import RegistrationPage
from homepage import HomePage

headers = "gender, firstname, lastname, email, password"
data = [
        ("Male", "steve", "jobs", "steve.jobs@company.com", "Password123"),
        ("Female", "laura", "turner", "laura.turner@company.com", "Password123")
        ]

@mark.parametrize(headers, data)
def test_registration(setup_tear_down, gender, firstname, lastname, email, password):
    
    hp = HomePage(setup_tear_down)
    
    # click on register link on Homepage
    hp.click_register()

    rp = RegistrationPage(setup_tear_down)

    # call register_user function in RegistrationPage
    rp.register_user(gender, firstname, lastname, email, password, password)













# old approach

    #    sw = SeleniumWrapper(setup_tear_down)
    #    sw.click_element(("link text", "Register"))
    # 
    #    if gender == "Male":
    #        sw.click_element(("id", "gender-male"))
    #    else:
    #        sw.click_element(("id", "gender-female"))
    #
    #    sw.enter_text(("id", "FirstName"), value=firstname)
    #    sw.enter_text(("id", "LastName"), value=lastname)
    #    sw.enter_text(("name", "Email"), value=email)
    #    sw.enter_text(("id", "Password"), value=password)
    #    sw.enter_text(("id", "ConfirmPassword"), value=password)
    #    sw.click_element(("xpath", "//input[@value='Register']"))
    #

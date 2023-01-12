from selenium_wrapper import SeleniumWrapper
from pytest import mark

headers = "gender, fname, lname, email, password, confirmpassword"
data = [
    ("male", "steve", "jobs", "steve.jobs@company.com", "Password123", "Password123"),
    ("female", "laura", "turner", "laura.turner@company.com", "Password123", "Password123")
]

@mark.parametrize(headers, data)
def test_registration(setup_tear_down, gender, fname, lname, email, password, confirmpassword):
    sw = SeleniumWrapper(setup_tear_down)
    sw.click_element(("link text", "Register"))
    if gender == "male":
        sw.click_element(("id", "gender-male"))
    else:
        sw.click_element(("id", "gender-female"))
    sw.enter_text(("id", "FirstName"), value=fname)
    sw.enter_text(("id", "LastName"), value=lname)
    sw.enter_text(("id", "Email"), value=email)
    sw.enter_text(("id", "Password"), value=password)
    sw.enter_text(("id", "ConfirmPassword"), value=confirmpassword)
    sw.click_element(("xpath", "//input[@value='Register']"))


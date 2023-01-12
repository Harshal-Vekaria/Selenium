from selenium_wrapper import SeleniumWrapper
from pytest import mark

headers = "email, password"
data = [
        ("bill.gates@company.com", "Password123"),
        ("hello.world@company.com", "Password123"),
        ("steve.jobs@company.con", "Password123")
    ]


@mark.parametrize(headers, data)
def test_login(setup_tear_down, email, password):
    sw = SeleniumWrapper(setup_tear_down)
    sw.click_element(("link text", "Log in"))
    sw.enter_text(("id", "Email"), value=email)
    sw.enter_text(("id", "Password"), value=password)
    sw.click_element(("xpath", "//input[@value='Log in']"))

from lib import SeleniumWrapper
from pytest import mark
from loginpage import LoginPage
from homepage import HomePage

headers = "email, password"
data = [
        ("bill.gates@company.com", "Password123"),
        ("hello.world@company.com", "Password123"),
        ("steve.jobs@company.con", "Password123")
    ]

@mark.parametrize(headers, data)
def test_login(setup_tear_down, email, password):

    hp = HomePage(setup_tear_down)
    
    # Click on login link present on Homepage
    hp.click_login()

    lp = LoginPage(setup_tear_down)
    
    lp.login(email, password)


# old approach

#    # enter email address
#    sw.enter_text(("id", "Email"), value=email)   
#
#    # enter password
#    sw.enter_text(("id", "Password"), value=password)
#
#    # click on Login Button
#    sw.click_element(("xpath", "//input[@value='Log in']"))
#










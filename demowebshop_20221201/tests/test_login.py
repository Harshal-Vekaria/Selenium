from demowebshop_20221201.demowebshop.src.excelLib import read_data, read_headers
from pytest import mark
from demowebshop_20221201.demowebshop.pom.loginpage import LoginPage

headers = read_headers("Shopping", "test_login")
data = read_data("Shopping", "test_login")

@mark.parametrize(headers, data)
def test_login(_driver, email, password):
    lp = LoginPage(_driver)

    # Click on Login Link
    lp.click_login_link()

    # Enter Username and Password
    lp.enter_email(email)
    lp.enter_password(password)

    # Click on Login
    lp.click_login_button()

    # Verify User login
    lp.verify_user_login(email)

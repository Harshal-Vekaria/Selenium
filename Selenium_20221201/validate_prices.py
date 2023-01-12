from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("https://demowebshop.tricentis.com")
sleep(5)
# ====================================================================================================================
# maintaining a dictioanry of product name and its corresponding expected price
products = {
         '14.1-inch Laptop': 1590.00, 
         'Build your own cheap computer': 800.00,
         'Build your own computer': 1200.00, 
         'Simple Computer': 500.00, 
         'Build your own expensive computer': 1800.00,
         '$25 Virtual Gift Card': 25.00
         }

for product, expected_price in products.items():
    _xpath = f"//a[text()='{product}']/../..//span[@class='price actual-price']"
    actual_price = driver.find_element_by_xpath(_xpath).text
    if float(actual_price) == expected_price:
        print('PASS')
    else:
        print(f'FAIL: the actual price of {product} is {actual_price} but expected price is {expected_price}')
    sleep(1)


# driver.find_element_by_xpath("//td[text()='C#']/..//input[@name='download']").click()

# driver.find_element_by_xpath("//a[text()='Python 3.10.0']/../..//a[text()='Release Notes']").click()

# books = ['Fiction', 'Health Book']

#for book in books:
#    sleep(4)
#    # dynamic xpath
#    _xpath = f"//a[text()='{book}']/../..//input[@value='Add to cart']"
#    driver.find_element_by_xpath(_xpath).click()
#

#====================================================================================================================
# close browser session
#sleep(2)
#driver.close()


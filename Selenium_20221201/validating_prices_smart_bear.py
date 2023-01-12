from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
from csv import reader
from re import findall

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
sleep(15)
# ====================================================================================================================

def read_prices():
    items = []
    with open(r'/Users/sandeep/Desktop/training/_selenium/data_files/smart_prices.csv') as f:
        rows = reader(f)
        headers = next(rows)    # skipping the headers
        return { row[0]: float(row[1]) for row in rows }

# taking the product name and price tag into python datastructure
data = read_prices()

for product, expected_price in data.items():
    # dynamic xpath
    _xpath = f"//span[text()='{product}']/../../..//span[@class='art-price' or @class='art-price art-price--offer']"
    price_tags = driver.find_elements_by_xpath(_xpath) 
    for item in price_tags:
        temp_tag = item.text
        
        # clean up the text or price tag
        price_tag = findall(r"[\d\.]", temp_tag)
        actual_price = float("".join(price_tag))
        
        # vaidate the price tag of each procuct
        if actual_price == expected_price:
            print("PASS")
        else:
            print(f"FAIL: product: {product}, expected_price: {expected_price}:: actual_price: {actual_price}")
        sleep(1)







































## maintaining a dictioanry of product name and its corresponding expected price
#products = {
#         '14.1-inch Laptop': 1590.00, 
#         'Build your own cheap computer': 800.00,
#         'Build your own computer': 1200.00, 
#         'Simple Computer': 500.00, 
#         'Build your own expensive computer': 1800.00,
#         '$25 Virtual Gift Card': 25.00
#         }
#
#for product, expected_price in products.items():
#    _xpath = f"//a[text()='{product}']/../..//span[@class='price actual-price']"
#    actual_price = driver.find_element_by_xpath(_xpath).text
#    if float(actual_price) == expected_price:
#        print('PASS')
#    else:
#        print(f'FAIL: the actual price of {product} is {actual_price} but expected price is {expected_price}')
#    sleep(1)
#

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


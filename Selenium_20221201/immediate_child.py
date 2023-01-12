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
driver.get("https://www.monsterindia.com/")
sleep(10)
#====================================================================================================================

driver.find_element_by_id("SE_home_autocomplete").send_keys("Python")
sleep(2)

driver.find_element_by_xpath("//input[@value='Search']").click()
sleep(10)

titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
companies = driver.find_elements_by_xpath("//span[@class='company-name']/a")

# finds all the job title links which are specific to JP Morgan
jp = driver.find_elements_by_xpath("//a[text()='JP Morgan Chase & Co.']/../../h3/a")

for title, company in zip(titles, companies):
    print(title.text, company.text)
    sleep(0.5)

print("---"*30)

for item in jp:
    print(item.text)
    sleep(0.2)






# get all the links present in the left navigation pane of demowebshop
#links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")

# find all the links present on the footer of the webpage
# links = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")

# find all the links present on footer of smartbaer webpage
#links = driver.find_elements_by_xpath("//div[@class='footer-main-wrapper']//a")

#for link in links:
#    # for each link print the link text
#    print(link.text)
#    sleep(1)
































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


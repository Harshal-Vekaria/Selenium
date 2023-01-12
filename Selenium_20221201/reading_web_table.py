from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
from csv import reader
from re import findall
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, title_is

# Instantiate a new chrome browser session
driver = Chrome("./chromedriver")
#driver.implicitly_wait(10)
# maximize the browser 
driver.maximize_window()
# launch URL
driver.get("file:///Users/sandeep/Desktop/training/_selenium/demo-html/demo.html")
sleep(5)
#====================================================================================================================
companies = ['FB', 'AAPL', 'MSFT', 'AA']

for company in companies:
    print(f"{company:>15}", end="")

print()
print("-"*70)

while True: # Monitor for ever  (inifinite for loop)
    for company in companies:
        _xpath = f"//td[text()='{company}']/..//td[@class='price']"
        share_price = driver.find_element_by_xpath(_xpath).text
        print(f"{share_price:>15}", end="")
    print()
    sleep(2)


#====================================================================================================================
# close browser session
#sleep(2)
#driver.close()


# CSS SELECTOR
# In CODE: tagname[attribute = 'value']         IN CONSOLE: $("tagname[attribute = 'value'])
#                   Only give tagnme#ID    OR    Only give tagname.class (if classname has spaces, replace them with ,)
#  CSS Selector Syntax Without Tag Name --->    [attribute=value]


# X-PATH
# In CODE: //tagname[@attribute = 'value']      IN CONSOLE: $x("tagname[attribute = 'value'])  Eg: $x("//input[@type = 'submit']")
# XPATH Locator Without Tag Name -->   //*[@attribute=value]
# XPATH based on text  --->     //tagname[contains(text(), ‘actual-text’)]
# //*[contains(attribute_name,'attribute_value')]       OR  //tagname[contains(attribute_name,'attribute_value')]
# //tagname[text()='actual-text']   --> Not recommended. Text can be changed by developer
# Traversing from child to parent to child   //tagname[@attribute = 'value']/parent::tagname/parent::tagname/tagname[index]/tagname

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(15)

dropdownDriver = Select(driver.find_element_by_xpath("//form[@class = 'ng-untouched ng-pristine ng-invalid']/div/select"))
dropdownDriver.select_by_index(1)

driver.find_element_by_css_selector("input[name='name']").send_keys("Dev")
driver.find_element_by_name("email").send_keys("gmail.com")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type = 'submit']").click()

assert "success" in driver.find_element_by_css_selector("div[class*='alert-success']").text
driver.quit()

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com")
driver.implicitly_wait(15)

driver.find_element_by_css_selector("#username").send_keys("Dev")
driver.find_element_by_css_selector(".password").send_keys("password")
driver.find_element_by_xpath("//a[contains(text(), 'Forgot Your Password?')]").click()
driver.find_element_by_xpath("//*[@value='Cancel']").click()
print(driver.find_element_by_xpath("//span[text()='Salesforce']").text)


driver.quit()




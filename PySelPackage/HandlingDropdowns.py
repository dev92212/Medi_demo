import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(15)

# --> SELECT can only be used when dropdown is defined in <select> tag
dropdownDriver = Select(driver.find_element_by_xpath("//form[@class = 'ng-untouched ng-pristine ng-invalid']/div/select"))
dropdownDriver.select_by_index(1)
#time.sleep(5)
#dropdownDriver.select_by_visible_text("Male")
#dropdownDriver.select_by_value("M")   #--> find "value" from the dropdown option tag.

# driver.quit()
#
# driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/dropdownsPractise")
# driver.implicitly_wait(15)
#
# driver.find_element_by_xpath("//div[@id = 'select-class-example']/fieldset/input").send_keys("in")
# time.sleep(2)
#
# for i in driver.find_elements_by_css_selector("ul[id = 'ui-id-1'] li a"):
#     if i.text == "India":
#         i.click()
#         break
#
# assert driver.find_element_by_xpath("//div[@id='select-class-example']/fieldset/input").get_attribute("value") == "India", "FAIL!"
#
# driver.quit()
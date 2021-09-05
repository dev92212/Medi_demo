import time

from selenium import webdriver

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cruxintelligence.com/")
driver.implicitly_wait(15)
driver.find_element_by_id("hs-eu-confirmation-button").click()


# Creating XPATH by traversing tags::
# Syntax: Parent-Tag Xpath]/Child-Tag[index]
driver.find_element_by_xpath("//div[@id = 'wrapper-footer']/div/div/div/a[2]").click()


# Creating CSS selector by traversing tags::
# Syntax: [Parent-Tag CSS] Child-Tag:nth-child(index)


#driver.quit()

from selenium import webdriver

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(15)

# For CheckBoxes
for i in driver.find_elements_by_xpath("//body/div[@class = 'block large-row-spacer']/div[4]/fieldset/label/input"):
    if i.get_attribute("value") == "option2":  #--> Remove IF for Checking all the boxes
        i.click()
        assert i.is_selected(), "Checkbox not selected!"

# For RadioButtons
driver.find_elements_by_xpath("//body/div[@class = 'block large-row-spacer']/div[1]/fieldset/label/input")[2].click()
assert driver.find_elements_by_xpath("//body/div[@class = 'block large-row-spacer']/div[1]/fieldset/label/input")[2].is_selected(), "FAIL!"

# for i in driver.find_elements_by_xpath("//body/div[@class = 'block large-row-spacer']/div[1]/fieldset/label/input"):
#     if i.get_attribute("value") == "radio3":
#         i.click()
#         assert i.is_selected(), "Radiobutton not selected!"



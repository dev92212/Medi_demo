import time
from selenium import webdriver

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(15)

driver.find_element_by_xpath("//div[@class = 'block large-row-spacer']/div[3]/fieldset/input[1]").send_keys("Dev")
driver.find_element_by_xpath("//div[@class = 'block large-row-spacer']/div[3]/fieldset/input[2]").click()
alertObj = driver.switch_to.alert
print(alertObj.text)
time.sleep(3)
assert "Dev" in alertObj.text, "Text not present!"
alertObj.accept()
#alertObj.dismiss()

driver.quit()

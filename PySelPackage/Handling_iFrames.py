from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
#driver.implicitly_wait(15)             #---> Implicit Wait
wait = WebDriverWait(driver, 5)         #---> Explicit Wait
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'File')]")))
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_xpath("//body/p").clear()
driver.find_element_by_xpath("//body/p").send_keys("DEV MISHRA")
driver.switch_to.default_content()
driver.find_element_by_xpath("//span[contains(text(),'File')]").click()

driver.quit()
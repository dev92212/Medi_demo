from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(15)             #---> Implicit Wait

mouse_action = ActionChains(driver)     #---> For Mouse Hover actions
mouse_action.move_to_element(driver.find_element_by_xpath("//div/div/fieldset/div/button[@id='mousehover']")).perform()
time.sleep(2)
mouse_action.move_to_element(driver.find_element_by_xpath("//div[@class = 'mouse-hover-content']/a[1]")).click().perform()

driver.quit()

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()   #---> Right click
action.double_click(driver.find_element_by_id("double-click")).perform()    #---> Double click

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()


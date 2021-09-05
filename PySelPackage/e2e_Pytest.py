from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chromeSetup = webdriver.ChromeOptions()
chromeSetup.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe", options=chromeSetup)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(15)             #---> Implicit Wait

# NOT FINISHED #
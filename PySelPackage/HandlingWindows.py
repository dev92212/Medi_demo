from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
#driver.implicitly_wait(15)             #---> Implicit Wait
wait = WebDriverWait(driver, 5)         #---> Explicit Wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Multiple Windows")))
driver.find_element_by_link_text("Multiple Windows").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[class = 'large-12 columns'] div a")))
driver.find_element_by_css_selector("div[class = 'large-12 columns'] div a").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.find_element_by_css_selector("div[class = 'large-12 columns'] div a").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.refresh()
time.sleep(3)
driver.quit()

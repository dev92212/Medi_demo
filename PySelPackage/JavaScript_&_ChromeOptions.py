from selenium import webdriver

chromeSetup = webdriver.ChromeOptions()
chromeSetup.add_argument("--ignore-certificate-errors")
chromeSetup.add_argument("--headless")

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe", options=chromeSetup)
# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions       <-- For Examples

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.implicitly_wait(15)

driver.find_element_by_css_selector("input[name='name']").send_keys("Dev")
print(driver.find_element_by_css_selector("input[name='name']").get_attribute("value"))

# ---> Javascript through DOM model         (execute_script) will execute any kind of javaScript
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
#driver.execute_script("arguments[0].click();", driver.execute_script("return document.getElementsByClassName('nav-link')[1]"))
driver.execute_script("arguments[2].click();", driver.execute_script("return document.getElementsByClassName('nav-link')[1]"),
                      driver.execute_script("return document.getElementsByClassName('nav-link')[0]"),
                      driver.execute_script("return document.getElementsByClassName('nav-link')[1]"))

driver.execute_script("window.scrollBy(0, 20);")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

from selenium import webdriver

driver = webdriver.Firefox(executable_path="E:\Browsers\geckodriver.exe")
#driver = webdriver.Edge(executable_path="E:\\Browsers\\msedgedriver.exe")  ---> Not Working
#driver = webdriver.Ie("E:\Browsers\IEDriverServer.exe")
#driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.efi.com")
driver.implicitly_wait(15)

print(driver.title)
driver.get("https://www.youtube.com")
driver.back()
driver.refresh()
print(driver.current_url)

driver.quit()
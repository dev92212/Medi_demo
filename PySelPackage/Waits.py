from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome("E:\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise")
#driver.implicitly_wait(15)             #---> Implicit Wait

driver.find_element_by_xpath("//header/div/div[2]/form/input").send_keys("ber")
time.sleep(2)
#assert len(driver.find_elements_by_xpath("//div[@class = 'products-wrapper']/div[1]/div")) == 3, "Incorrect number of products"

productsAdded_List = []
for i in driver.find_elements_by_xpath("//div[@class = 'product-action']/button"):
    productsAdded_List.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()

driver.find_element_by_css_selector("div[class = 'cart'] a img").click()
driver.find_element_by_css_selector("div[class = 'cart'] div div button").click()

wait = WebDriverWait(driver, 15)        #---> Explicit Wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input.promoCode")))        #---> Explicit Wait

productsInCart_List = []
for i in driver.find_elements_by_xpath("//table[@id = 'productCartTables']/tbody/tr/td[2]/p"):
    productsInCart_List.append(i.text)

assert productsAdded_List == productsInCart_List

sum_of_seperateAmounts = 0

for i in driver.find_elements_by_xpath("//tr/td[5]/p"):
    sum_of_seperateAmounts = sum_of_seperateAmounts + int(i.text)

assert float(sum_of_seperateAmounts) == float(driver.find_element_by_xpath("//span[@class = 'totAmt']").text), "Total amount doesn't match"

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class = 'promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'promoWrapper']/span"))) #---> Explicit Wait

assert driver.find_element_by_xpath("//div[@class = 'promoWrapper']/span").text == "Code applied ..!"

#totalAmt = driver.find_element_by_xpath("//span[@class = 'totAmt']").text

discount = driver.find_element_by_xpath("//span[@class = 'discountPerc']").text
discount = ''.join(e for e in discount if e.isalnum())

#amtAfterDiscount = driver.find_element_by_xpath("//span[@class = 'discountAmt']").text

assert float(driver.find_element_by_xpath("//span[@class = 'totAmt']").text) - float((float(discount)*float(driver.find_element_by_xpath("//span[@class = 'totAmt']").text))/100) == float(driver.find_element_by_xpath("//span[@class = 'discountAmt']").text), "Amounts do not match!"

driver.quit()
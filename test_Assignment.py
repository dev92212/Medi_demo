import pytest
from selenium.webdriver.support.select import Select
import time
from baseClass import baseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("Dataload_orderPlacement")
@pytest.mark.usefixtures("Dataload_medDetails")
@pytest.mark.usefixtures("Dataload_login")
@pytest.mark.usefixtures("Dataload_existingOrderActions")
class TestMedpay_Dashbaord(baseClass):

    # TEST SCENARIO: User can Login to the web application
    def test_loginPage(self, Dataload_login):
        logs = self.getLogger()
        try:
            self.driver.find_element_by_id("username").send_keys(Dataload_login[0])
            self.driver.find_element_by_id("password").send_keys(Dataload_login[1])
            self.driver.find_element_by_xpath("//button[@class = 'chakra-button css-1kz2znw']").click()
            time.sleep(2)
            assert "Logged in" in self.driver.find_element_by_xpath("//div[@id = 'root']/div[1]/p").text
            logs.info("LOGGED IN")

        except Exception as ex:
            logs.critical("Login failed:", ex)

    # TEST SCENARIO: User can enter all the details and place an order
    def test_placingOrder(self, Dataload_orderPlacement, Dataload_medDetails):
        logs = self.getLogger()
        try:
            self.driver.find_element_by_xpath("//button[@class = 'chakra-button css-11hsy1o']").click()
            self.driver.find_element_by_id("partner_order_id").send_keys(Dataload_orderPlacement[0])
            dropdowns = self.driver.find_elements_by_xpath("//select[@class = 'chakra-select css-56bspj']")
            for i in dropdowns:
                if i.is_enabled():
                    Select(i).select_by_index(1)

            self.driver.find_element_by_id("name").send_keys(Dataload_orderPlacement[1])
            self.driver.find_element_by_id("mobile").send_keys(Dataload_orderPlacement[2])
            self.driver.find_element_by_id("alternative_mobile").send_keys(Dataload_orderPlacement[3])
            self.driver.find_element_by_id("email").send_keys(Dataload_orderPlacement[4])
            self.driver.find_element_by_id("address").send_keys(Dataload_orderPlacement[5])
            self.driver.find_element_by_id("landmark").send_keys(Dataload_orderPlacement[6])
            self.driver.find_element_by_id("pin_code").send_keys(Dataload_orderPlacement[7])
            self.driver.find_element_by_id("city").send_keys(Dataload_orderPlacement[8])
            self.driver.find_element_by_id("state").send_keys(Dataload_orderPlacement[9])

            self.driver.find_element_by_css_selector("input[width = '500']").send_keys(Dataload_orderPlacement[11])
            self.explicitWaitforElementPresence("//div[@class = 'chakra-stack css-a9porv']/div/img")
            self.driver.find_element_by_id("doctor").send_keys(Dataload_orderPlacement[10])

            for i in range(len(Dataload_medDetails)):
                self.driver.find_element_by_id("react-select-3-input").send_keys(Dataload_medDetails[i])
                self.explicitWaitforElementPresence("//div[@class = ' css-2b097c-container']/div[2]/div/div/div/p")

                for j in self.driver.find_elements_by_xpath("//div[@class = ' css-2b097c-container']/div[2]/div/div/div/p"):
                    if "1 Kg" in j.text:
                        j.click()
                        break
                    elif "546.80" in j.text:
                        j.click()
                        break
                    elif "390.00" in j.text:
                        j.click()
                        break
                    elif "1290.00" in j.text:
                        j.click()
                        break

            med_cost = 0.0
            for i in self.driver.find_elements_by_xpath("//input[@placeholder= 'Amount']"):
                med_cost = med_cost + float(i.get_attribute("value"))

            assert med_cost == float(self.driver.find_element_by_xpath("//table[@role= 'table']/tbody/tr/td[2]/p").text)
            logs.info("Bill Amount verified")
            self.driver.find_element_by_xpath("//button[text()='Submit']").click()
            logs.info("Order Placed")

        except Exception as ex:
            logs.error("Order placement failed:", ex)

    # TEST SCENARIO: User can view their order and all its details
    def test_viewOrderStatus(self, Dataload_existingOrderActions):
        logs = self.getLogger()

        try:
            ii = 1
            for i in self.driver.find_elements_by_xpath("//table[@role = 'table']/tbody/tr/td[1]/div/div/button"):
                if i.text == str(Dataload_existingOrderActions[0]):
                    print(self.driver.find_element_by_xpath("//table[@role = 'table']/thead/tr/th[1]/p").text, ":", i.text)
                    print(self.driver.find_element_by_xpath("//table[@role = 'table']/thead/tr/th[2]/p").text, ":",
                          self.driver.find_element_by_xpath("//table[@role = 'table']/tbody/tr["+str(ii)+"]/td[2]").text)
                    print(self.driver.find_element_by_xpath("//table[@role = 'table']/thead/tr/th[3]").text, ":",
                          self.driver.find_element_by_xpath("//table[@role = 'table']/tbody/tr["+str(ii)+"]/td[3]").text)
                    print(self.driver.find_element_by_xpath("//table[@role = 'table']/thead/tr/th[4]").text, ":",
                          self.driver.find_element_by_xpath("//table[@role = 'table']/tbody/tr["+str(ii)+"]/td[4]").text)
                    break
                ii = ii + 1

        except Exception as ex:
            logs.error("Error in order status:", ex)

    # TEST SCENARIO: User can cancel their order
    def test_orderCancellation(self, Dataload_existingOrderActions):
        logs = self.getLogger()
        try:
            ii = 1
            for i in self.driver.find_elements_by_xpath("//table[@role = 'table']/tbody/tr/td[1]/div/div/button"):
                if i.text == str(Dataload_existingOrderActions[0]):
                    self.driver.find_element_by_xpath("//table[@role = 'table']/tbody/tr["+str(ii)+"]/td[6]/button").click()
                    self.driver.find_element_by_xpath("//footer/button[2]").click()
                    Select(self.driver.find_element_by_id("reason")).select_by_index(2)
                    self.driver.find_element_by_css_selector("form[class = 'css-0'] button").click()
                    break

            self.explicitWaitforElementPresence("//div[@id = 'root']/div[1]/p")
            assert "Order cancelled" in self.driver.find_element_by_xpath("//div[@id = 'root']/div[1]/p").text
            logs.info("Order cancelled")

        except Exception as ex:
            logs.error("Error in order cancellation:", ex)

    # TEST SCENARIO: User can logout successfully
    def test_logout(self):
        logs = self.getLogger()
        try:
            self.driver.find_element_by_xpath("//button[@aria-label = 'Search database']").click()
            self.explicitWaitforElementPresence("//div[@id = 'chakra-modal--body-95']/button[3]")
            self.driver.find_element_by_xpath("//div[@id = 'chakra-modal--body-95']/button[3]").click()
            self.driver.switch_to.alert.accept()
            self.explicitWaitforElementPresence("//label[@id = 'field-469-label']")
            assert "amplifyapp.com/login" in self.driver.current_url
            logs.info("Logged out successfully")

        except Exception as ex:
            logs.error("Error in Logout:", ex)
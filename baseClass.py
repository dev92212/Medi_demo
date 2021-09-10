import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class baseClass:
    def getLogger(self):
        testcaseName = inspect.stack()[1][3]
        logger = logging.getLogger(testcaseName)

        fileHandler = logging.FileHandler("logfile.log")
        logFormat = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(levelname)s: %(message)s")
        fileHandler.setFormatter(logFormat)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger

    def explicitWaitforElementPresence(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))

import inspect
import logging
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PO.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:
    # all of these will be reused to help search for multiple items without manually writing this for each one!

    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0, 200);")

    def scrollUp(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

    def searchItem(self, data):
        self.driver.find_element(By.CSS_SELECTOR, "#search").send_keys(data)  # (*HomePage.item_search)

    def clearSearch(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search")))
        self.driver.find_element(By.CSS_SELECTOR, "#search").click()
        self.driver.find_element(By.CSS_SELECTOR, "#search").clear()

    def clickSearch(self):
        self.driver.find_element(By.XPATH, "//button[@aria-label='go']").click()

    def addToCart(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']")))
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()

    def continueShopping(self):
        self.driver.find_element(By.XPATH, ".//button[@aria-label='close']").click()

    def findItem(self):
        log = self.getLog()
        # helps keep track of the index of each element in data
        i = -1
        ratings = HomePage.searchResults(self)
        for rating in ratings:
            i += 1
            if int(rating.text) > 1000:
                log.info("Item was found at index " + str(i))
                break

        time.sleep(2)
        # executing javscript code in order to scroll desired item into view to add to cart
        self.driver.execute_script("arguments[0].scrollIntoView(true);", rating)
        ratings[i].click()
        time.sleep(3)
        self.addToCart()


    def getLog(self):
        loggerName = inspect.stack()[1][3]  # Gets the name of the class / method from where this method is called
        logger = logging.getLogger(loggerName)
        # formatter will produce...201-19-02-17 12:40:14,798 : ERROR: <testcasename>: Fatal error in submitting credit card payment on step 4. Cannot continue...using for formatting error logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler('logfile.log')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
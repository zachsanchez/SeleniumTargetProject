import time
import pytest
from selenium.webdriver.common.by import By
from PO.HomePage import HomePage
from TestData.SearchData import SearchData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTarget(BaseClass):

    def test_groceryShopping(self, getData):
        log = self.getLog()
        wait = WebDriverWait(self.driver, 15)
        log.info("Searching for first item: BREAD")
        time.sleep(2)

        self.searchItem(getData["item1"])
        time.sleep(1.4)
        self.clickSearch()
        self.findItem()
        log.info("BREAD was found and added to cart")
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[@aria-label='close']")))
        self.continueShopping()

        time.sleep(2)
        self.clearSearch()
        log.info("Searching for second item: MILK")

    @pytest.fixture(params=SearchData.test_search_data)
    def getData(self, request):
        return request.param
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PO.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    cart_button = (By.XPATH, "//a[text()='View cart & check out']")
    # # grabs all rating counts of items populating on page after search
    # search_results = (By.XPATH, "(//span[@class='RatingStars__RatingCount-sc-k7ad82-1 jdkOOw'])")
    #
    # def searchResults(self):
    #     return self.driver.find_elements(*HomePage.search_results)

    def goToCheckout(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View cart & check out']")))
        self.driver.find_element(*HomePage.cart_button).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
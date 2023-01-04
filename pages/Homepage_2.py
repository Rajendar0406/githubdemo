import time

from selenium.webdriver.common.by import By
from base.basedriver import BaseDriver

class HomePage2(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    PRODUCTSMENU = "//div[contains(@class, 'shop-menu')]//ul//li[2]//a"
    ALLPRODUCTSTEXT = "//div[@class='features_items']//h2"
    SEARCHPRODUCTS = "//input[@id='search_product']"
    SUBMITSEARCH = "//button[@id='submit_search']"
    SEARCHOUTPUT = "//div[@class='features_items']/h2"
    SEARCHRESULTS = "//div[contains(@class, 'productinfo')]//p"

    def getProductsclick(self):
        return self.driver.find_element(By.XPATH, self.PRODUCTSMENU)
    def getProductsPageVerify(self):
        return self.driver.find_element(By.XPATH, self.ALLPRODUCTSTEXT)
    def getsearchProducts(self):
        return self.driver.find_element(By.XPATH, self.SEARCHPRODUCTS)
    def getsubmitbutton(self):
        return self.driver.find_element(By.XPATH, self.SUBMITSEARCH)
    def getsearchVerifyText(self):
        return self.driver.find_element(By.XPATH, self.SEARCHOUTPUT)
    def getsearchresults(self):
        return self.driver.find_elements(By.XPATH, self.SEARCHRESULTS)

    def clickProductPageverify(self):
        self.getProductsclick().click()
        productspageUrl = "https://automationexercise.com/products"
        if self.driver.current_url != productspageUrl:
            self.driver.get(productspageUrl)

    def assertsearchProducts(self):
        self.getProductsPageVerify()
        print("*****", self.getProductsPageVerify().text, "*****")

    def searchProducts(self):
        self.getsearchProducts().send_keys("Jeans")

    def submitSearch(self):
        self.getsubmitbutton().click()

    def assertSearchedpage(self):
        self.getsearchVerifyText()
        print("*****", self.getsearchVerifyText().text, "*****")
        assert self.getsearchVerifyText().text == "SEARCHED PRODUCTS"

    def searchedProducts(self):
        searchresults = self.getsearchresults()
        print(len(searchresults))
        for product in searchresults:
            print(product.text)

    def productSearchAndVerify(self):
        self.clickProductPageverify()
        self.assertsearchProducts()
        self.searchProducts()
        self.submitSearch()
        self.assertSearchedpage()
        self.searchedProducts()


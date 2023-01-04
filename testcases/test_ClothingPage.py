import pytest
from selenium import webdriver
from pages.Homepage_2 import HomePage2


class TestClothingProducts:

    def test_product_search_2(self):

        self.driver = webdriver.Chrome(executable_path="C:\\Users\\raikoderajendar\chromedriver.exe")
        self.driver.get("http://automationexercise.com")
        self.driver.maximize_window()
        self.Hp2 = HomePage2(self.driver)
        self.Hp2.productSearchAndVerify()

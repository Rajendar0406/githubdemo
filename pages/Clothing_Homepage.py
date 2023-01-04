from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

option = Options()
option.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path="C:\\Users\\raikoderajendar\chromedriver.exe", chrome_options=option)
Url = "http://automationexercise.com"
driver.get(Url)
driver.maximize_window()

ProductsMenu = driver.find_element(By.XPATH, "//div[contains(@class, 'shop-menu')]//ul//li[2]//a")
ProductsMenu.click()
productspageUrl = "https://automationexercise.com/products"
if driver.current_url != productspageUrl:
    driver.get(productspageUrl)

AllProductsText = driver.find_element(By.XPATH, "//div[@class='features_items']//h2")
print("*****", AllProductsText.text, "*****")

searchProducts = driver.find_element(By.XPATH, "//input[@id='search_product']")
searchProducts.send_keys("Jeans")

submitSearch = driver.find_element(By.XPATH, "//button[@id='submit_search']")
submitSearch.click()

SearchOutput = driver.find_element(By.XPATH, "//div[@class='features_items']/h2")
print("*****", SearchOutput.text, "*****")
assert SearchOutput.text == "SEARCHED PRODUCTS"

searchresults = driver.find_elements(By.XPATH, "//div[contains(@class, 'productinfo')]//p")

for product in searchresults:
    print(product.text)


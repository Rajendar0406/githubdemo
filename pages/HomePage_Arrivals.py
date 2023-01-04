import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#def test_CheckHomePageArrivals():
from selenium.webdriver.support.wait import WebDriverWait

option = Options()
option.add_argument('--disable-notifications')

driver = webdriver.Chrome(executable_path="C:\\Users\\raikoderajendar\chromedriver.exe", chrome_options=option)
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
Shop_Click = driver.find_element(By.LINK_TEXT, "Shop")
Shop_Click.click()
if driver.current_url == "https://practice.automationtesting.in/#google_vignette":
    print("Updating the url")
    driver.get("https://practice.automationtesting.in/shop/")

Home_menu_Click = driver.find_element(By.XPATH, "//nav[@class = 'woocommerce-breadcrumb']//a")
Home_menu_Click.click()

if driver.current_url == "https://practice.automationtesting.in/shop/#google_vignette":
    print("Updating the url")
    driver.get("https://practice.automationtesting.in")

print("Checking the arrivals")
wait = WebDriverWait(driver, 5)

Arrivals = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'woocommerce']//ul//li//a//img")))\
    .find_elements(By.XPATH, "//div[@class = 'woocommerce']//ul//li//a//img")
#Arrivals = driver.find_elements(By.XPATH, "//div[@class = 'woocommerce']//ul//li//a//h3")
#driver.execute_script("arguments[0].scrollIntoView();",Arrivals)
print(len(Arrivals))

assert len(Arrivals) == 3

print("The Homepage contains 3 Arrivals only")

Product = input("Enter the product to add to cart:")
for arrival in Arrivals:
    #if arrival.get_attribute("title") == 'Mastering JavaScript':
    if arrival.get_attribute("title") == Product:
        driver.execute_script("arguments[0].scrollIntoView();", arrival)
        arrival.click()

assert Product in driver.title

#Description testcase

Description = driver.find_element(By.XPATH, "//div[contains(@class, 'woocommerce-tabs')]//ul//li[1]//a")
Description.click()
#
time.sleep(3)

#Review testcase

Review = driver.find_element(By.XPATH, "//div[contains(@class, 'woocommerce-tabs')]//ul//li[2]//a")
Review.click()

#Adding product to basket testcase

Product_AddToCart = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to basket')]")
Product_AddToCart.click()

View_Bucket = driver.find_element(By.XPATH, "//div[@class = 'woocommerce-message']//a")
View_Bucket.click()

product_check = driver.find_element(By.XPATH, "//table[contains(@class, 'shop_table')]//tbody//tr//td[3]//a")
assert product_check.text == 'Mastering JavaScript'
print("Added item validated")

subtotal = driver.find_element(By.XPATH, "//tr[@class='cart-subtotal']//td//span")
print(subtotal.text)

Tax = driver.find_element(By.XPATH, "//tr[contains(@class, 'tax-rate')]//td//span")
print(Tax.text)
#Total = subtotal + Tax

Total1 = driver.find_element(By.XPATH, "//tr[contains(@class, 'order-total')]//td//span")
print(Total1.text)


Proceed_to_Checkout = driver.find_element(By.XPATH, "//div[@class = 'wc-proceed-to-checkout']//a")
Proceed_to_Checkout.click()
driver.implicitly_wait(3)

Firstname = driver.find_element(By.ID, "billing_first_name").send_keys("Messi")
Lastname = driver.find_element(By.ID, "billing_last_name").send_keys("Leonel")

emailId = driver.find_element(By.ID, "billing_email")
emailId.send_keys("abcd123@gmail.com")
time.sleep(2)

Phone = driver.find_element(By.ID, "billing_phone")
Phone.send_keys("9977886644")

wait = WebDriverWait(driver, 10)
Country_name = wait.until(EC.element_to_be_clickable((By.ID, "select2-chosen-1")))
Country_name.click()
Country_name_textField= wait.until(EC.element_to_be_clickable((By.ID, "s2id_autogen1_search")))
Country_name_textField.send_keys("Arg")
time.sleep(2)

Countries = driver.find_elements(By.XPATH, "//ul[@id = 'select2-results-1']//li")

for country in Countries:
    if country.text == "Argentina":
        country.click()

print("Country is selected")

Address = driver.find_element(By.NAME, "billing_address_1")
Address.send_keys("FlatNo-44, Golden Mellinium, Vasanth Nagar")

City = driver.find_element(By.NAME, "billing_city")
City.send_keys("Bangalore")

StateClick = driver.find_element(By.XPATH, "//div[contains(@class, 'state_select')]//a//span")
StateClick.click()
State = driver.find_element(By.ID, "s2id_autogen2_search")
State.send_keys("Sal")

States = driver.find_elements(By.XPATH, "//ul[@id ='select2-results-2']//li")
for state1 in States:
    if state1.text == "Salta":
        state1.click()
print("State is selected")


Pincode = driver.find_element(By.XPATH, "//input[@id = 'billing_postcode']")
Pincode.send_keys("560052")
print("Address details are updated")

Payments_modes = driver.find_elements(By.XPATH, "//div[@id = 'payment']//ul//li//input")

for payment in Payments_modes:
    if payment.get_attribute("value") == "cod":
        payment.click()
        assert payment.is_selected()
print("Payment method selected")

#wait = WebDriverWait(driver, 5)
#PlaceOrder = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value = 'Place order']")))
time.sleep(5)
PlaceOrder = driver.find_element(By.XPATH, "//input[@value = 'Place order' and @id = 'place_order']")
PlaceOrder.click()

ConfirmationMessage = driver.find_element(By.XPATH, "//div[contains(@class, 'page-content')]//div[1]//p[1]")
print(ConfirmationMessage.text)
import time

from selenium.webdriver.common.by import By
from base.basedriver import BaseDriver

class CheckOutPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators

    FIRSTNAME = "billing_first_name"
    LASTNAME = "billing_last_name"
    EMAILID = "billing_email"
    PHONE = "billing_phone"
    COUNTRY_NAME = "select2-chosen-1"
    COUNTRY_NAME_TEXTFIELD = "s2id_autogen1_search"
    COUNTRIES = "//ul[@id = 'select2-results-1']//li"
    ADDRESS = "billing_address_1"
    CITY = "billing_city"
    STATECLICK = "//div[contains(@class, 'state_select')]//a//span"
    STATE = "s2id_autogen2_search"
    STATES = "//ul[@id ='select2-results-2']//li"
    PINCODE = "//input[@id = 'billing_postcode']"
    PAYMENTS_MODES = "//div[@id = 'payment']//ul//li//input"
    PLACEORDER = "place_order"
    CONFIRMATIONMESSAGE = "//div[contains(@class, 'page-content')]//div[1]//p[1]"

    def getFirstName(self):
        return self.driver.find_element(By.ID, self.FIRSTNAME)

    def getLastName(self):
        return self.driver.find_element(By.ID, self.LASTNAME)

    def getEmail(self):
        return self.driver.find_element(By.ID,self.EMAILID)

    def getPhoneNumber(self):
        return self.driver.find_element(By.ID, self.PHONE)

    def getCountryField(self):
        return self.wait_element_to_Clickable(By.ID, self.COUNTRY_NAME)

    def getCountryTextField(self):
        return self.wait_element_to_Clickable(By.ID, self.COUNTRY_NAME_TEXTFIELD)

    def getCountriesList(self):
        return self.driver.find_elements(By.XPATH, self.COUNTRIES)

    def getAddress(self):
        return self.driver.find_element(By.NAME, self.ADDRESS)

    def getCity(self):
        return self.driver.find_element(By.NAME, self.CITY)

    def getstateclick(self):
        return self.driver.find_element(By.XPATH, self.STATECLICK)

    def getstateTextenter(self):
        return self.driver.find_element(By.ID, self.STATE)

    def getStatesList(self):
        return self.driver.find_elements(By.XPATH, self.STATES)

    def getPincode(self):
        return self.driver.find_element(By.XPATH, self.PINCODE)
    def getPaymentModes(self):
        return self.driver.find_elements(By.XPATH, self.PAYMENTS_MODES)
    def getPlaceOrderclick(self):
        return self.driver.find_element(By.ID, self.PLACEORDER)


    def FirstNameLastName(self,firstname,lastname):
        self.getFirstName().send_keys(firstname)
        time.sleep(2)
        self.getLastName().send_keys(lastname)
        time.sleep(2)

    def EmailPhoneDetails(self,email,phone):
        self.getEmail().send_keys(email)
        time.sleep(2)
        self.getPhoneNumber().send_keys(phone)

    def CountrySelect(self,Country):
        self.getCountryField().click()
        self.getCountryTextField().send_keys(Country)
        countries = self.getCountriesList()
        for country in countries:
            if country.text == Country:
                country.click()
    print("Country is selected")

    def AddressFlatorHome(self,address):
        self.getAddress().send_keys(address)
        time.sleep(2)

    def CityName(self,city):
        self.getCity().send_keys(city)
        time.sleep(2)

    def stateDetails(self, statename):
        self.getstateclick().click()
        self.getstateTextenter().send_keys(statename)
        states = self.getStatesList()
        for state1 in states:
            if state1.text == statename:
                state1.click()
        time.sleep(2)

    def pincodedetails(self, pincode):
        self.getPincode().send_keys(pincode)
        time.sleep(2)

    def paymentSelection(self):
        paymentsList = self.getPaymentModes()
        for payment in paymentsList:
            if payment.get_attribute("value") == "cod":
                payment.click()
                assert payment.is_selected()
    print("Payment method is selected")
    time.sleep(2)

    def placeOrder(self):
        self.getPlaceOrderclick().click()

    def BillingAddressDetails(self, firstname, lastname, email, phone, Country, address, city,statename, pincode):
        self.FirstNameLastName(firstname, lastname)
        self.EmailPhoneDetails(email, phone)
        self.CountrySelect(Country)
        self.AddressFlatorHome(address)
        self.CityName(city)
        self.stateDetails(statename)
        self.pincodedetails(pincode)
        self.paymentSelection()
        self.placeOrder()



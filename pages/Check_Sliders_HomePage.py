import time
from selenium.webdriver.common.by import By
from base.basedriver import BaseDriver
from pages.CheckoutPage import CheckOutPage


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators

    Shop_Click_link = "Shop"
    Home_menu_Click = "//nav[@class = 'woocommerce-breadcrumb']//a"
    Slider_click = "//div[@class ='n2-ss-slider-1 n2-grab']//div//img"
    Arrivals_images = "//div[@class = 'woocommerce']//ul//li//a//img"
    Description_field = "//div[contains(@class, 'woocommerce-tabs')]//ul//li[1]//a"
    Review_field = "//div[contains(@class, 'woocommerce-tabs')]//ul//li[2]//a"
    Product_AddToCart = "//button[contains(text(), 'Add to basket')]"
    View_Bucket = "//div[@class = 'woocommerce-message']//a"
    product_check = "//table[contains(@class, 'shop_table')]//tbody//tr//td[3]//a"
    subtotal = "//tr[@class='cart-subtotal']//td//span"
    Tax = "//tr[contains(@class, 'tax-rate')]//td//span"
    Total1 = "//tr[contains(@class, 'order-total')]//td//span"
    Proceed_to_Checkout = "//div[@class = 'wc-proceed-to-checkout']//a"


    def getShopMenuClick(self):
        return self.driver.find_element(By.LINK_TEXT, self.Shop_Click_link)
        #Shop_Click.click()

    def getHomeMenuClick(self):
        return self.driver.find_element(By.XPATH, self.Home_menu_Click)

    def getSliderClick(self):
        return self.driver.find_elements(By.XPATH, self.Slider_click)

    def getArrivalsImages(self):
        return self.wait_elementClickable(By.XPATH, self.Arrivals_images)

    def getDescriptionField(self):
        return self.driver.find_element(By.XPATH, self.Description_field)

    def getReviewField(self):
        return self.driver.find_element(By.XPATH, self.Review_field)

    def getproducttoCart(self):
        return self.driver.find_element(By.XPATH, self.Product_AddToCart)

    def getViewBasket(self):
        return self.driver.find_element(By.XPATH, self.View_Bucket)

    def getProductCheck(self):
        return self.driver.find_element(By.XPATH, self.product_check)

    def getsubtotal(self):
        return self.driver.find_element(By.XPATH, self.subtotal)

    def getTax(self):
        return self.driver.find_element(By.XPATH, self.Tax)

    def gettotal(self):
        return self.driver.find_element(By.XPATH, self.Total1)

    def getProceedToCheckout(self):
        return self.driver.find_element(By.XPATH, self.Proceed_to_Checkout)


    def clickShopLink(self):
        self.getShopMenuClick().click()
        if self.driver.current_url == "https://practice.automationtesting.in/#google_vignette":
            print("Updating the url")
            self.driver.get("https://practice.automationtesting.in/shop/")
        print("Url updated to homepage")
        time.sleep(2)
        time.sleep(2)

    def clickHomeLink(self):
        self.getHomeMenuClick().click()

        print(self.driver.current_url)
        if self.driver.current_url == "https://practice.automationtesting.in/shop/#google_vignette":
            print("Updating the url")
            self.driver.get("https://practice.automationtesting.in")
        print("Url updated to homepage")
        time.sleep(2)

    def clickSliderimage(self):
        #self.getSliderClick().click()
        Sliders = self.driver.find_elements(By.XPATH, "//div[@class ='n2-ss-slider-1 n2-grab']//div//img")
        print(len(self.getSliderClick()))

        assert len(Sliders) == 3

        for i in range(len(Sliders)):
            Slider_click = self.driver.find_element(By.XPATH, "//div[@id='n2-ss-6-arrow-next']/img[@class='n2-ow']")
            Slider_click.click()
            time.sleep(2)

    def ArrivalsCountVerify(self):
        Arrivals = self.getArrivalsImages()\
    .find_elements(By.XPATH, self.Arrivals_images)

        assert len(Arrivals) == 3
        print("The Homepage contains 3 Arrivals only")

    def ArrivalproductClick(self):
        for arrival in self.getArrivalsImages().find_elements(By.XPATH, self.Arrivals_images):
            if arrival.get_attribute("title") == 'Mastering JavaScript':
                self.driver.execute_script("arguments[0].scrollIntoView();", arrival)
                arrival.click()

    def DescriptionDetails(self):
        self.getDescriptionField().click()
        print("Description is Read")
        time.sleep(3)

    def ReviewDetails(self):
        self.getReviewField().click()
        print("Review is read")

    def AddProductandView(self):
        print("Adding product to the basket")
        self.getproducttoCart().click()
        time.sleep(2)
        print("Viewing the added product in the basket")
        self.getViewBasket().click()

    def ProductCheck(self):
        Product_check = self.getProductCheck()
        assert Product_check.text == 'Mastering JavaScript'
        print("Added item validated")

    def Amountdisplay(self):
        print(self.getsubtotal().text)
        print(self.getTax().text)
        print(self.gettotal().text)

    def ProceedToCheckOut(self):
        self.getProceedToCheckout().click()
        #time.sleep(3)
        # Billing_Order_confirmation = CheckOutPage(self.driver)
        # return Billing_Order_confirmation

    def HomeProductActions(self):
        self.clickShopLink()
        self.clickHomeLink()
        self.clickSliderimage()
        self.ArrivalsCountVerify()
        self.ArrivalproductClick()
        self.DescriptionDetails()
        self.ReviewDetails()
        self.AddProductandView()
        self.ProductCheck()
        self.Amountdisplay()
        self.ProceedToCheckOut()

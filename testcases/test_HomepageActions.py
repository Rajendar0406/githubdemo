import pytest
import softest
from pages.Check_Sliders_HomePage import HomePage
from pages.CheckoutPage import CheckOutPage
from ddt import data, ddt, unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestSlidersAndArrivalsVerify(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.Hp = HomePage(self.driver)
        self.Cp = CheckOutPage(self.driver)
        self.ut = Utils()

    def test_sliders_check(self):
        self.Hp.clickShopLink()
        self.Hp.clickHomeLink()
        self.Hp.clickSliderimage()
    print("Testcase1 executed Successfully")

    def test_Arrivals_check(self):
        self.test_sliders_check()
        self.Hp.ArrivalsCountVerify()
    print("Testcase2 executed Successfully")

    def test_Arrival_Product_click(self):
        self.test_sliders_check()
        self.Hp.ArrivalsCountVerify()
        self.Hp.ArrivalproductClick()
    print("Testcase3 executed Successfully")

    def test_Description_Review(self):
        self.test_sliders_check()
        self.Hp.ArrivalsCountVerify()
        self.Hp.ArrivalproductClick()
        self.Hp.DescriptionDetails()
        self.Hp.ReviewDetails()
    print("Testcases 4,5 executed Successfully")

    def test_AddingAndViewProduct(self):
        self.test_sliders_check()
        self.Hp.ArrivalsCountVerify()
        self.Hp.ArrivalproductClick()
        self.Hp.AddProductandView()
    print("Testcases 6,7 executed Successfully")

    def test_productLogPage(self):
        self.test_AddingAndViewProduct()
        self.Hp.ProductCheck()
        self.Hp.Amountdisplay()
        self.Hp.ProceedToCheckOut()
    print("Testcases 8,9 executed Successfully")

    def test_product_search(self):
        self.Hp.HomeProductActions()
        print("Billing address details to enter")
        self.Cp.BillingAddressDetails("Messi", "Leonel", "messi123@gmail.com", "9988776655", "India", "FlatNo-44, Golden Mellinium, Vasanth Nagar", "Bangalore","Karnataka", "560052")
        print("Product1 ordered successfully")





    #@data(*Utils.read_data_from_excel("C:\\Users\\raikoderajendar\\PycharmProjects\\pythonProjectAssessment1\\testdata\\BillingAddressDetails.xlsx", "Details"))
    # @data(*Utils.read_data_from_csv("C:\\Users\\raikoderajendar\\PycharmProjects\\pythonProjectAssessment1\\testdata\\BillingAddressDetailscsv.csv"))
    # @unpack
    # def test_product_search(self, firstname, lastname, email, phone, address, city,statename, pincode):
    #     self.Hp.HomeProductActions()
    #     #self.Cp = CheckOutPage(self.driver)
    #     print("Billing address details to enter")
    #     self.Cp.BillingAddressDetails(firstname, lastname, email, phone, address, city,statename, pincode)

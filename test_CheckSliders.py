import pytest

from pages.Check_Sliders_HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = HomePage(self.driver)
        #self.ut = Utils()
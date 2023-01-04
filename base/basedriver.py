import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self,direction):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pagelength = document.body.scrollHeight")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);var pagelength = document.body.scrollHeight")
            if lastCount == pageLength:
                match = True
        time.sleep(4)

    def wait_elementClickable(self,by_locator,locator):
        wait = WebDriverWait(self.driver, 5)
        Arrivals = wait.until(EC.element_to_be_clickable((by_locator, locator)))
        return Arrivals

    def wait_element_to_Clickable(self,by_locator,locator):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.element_to_be_clickable((by_locator, locator)))

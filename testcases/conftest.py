import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope='class')
def setup(request, browser):
    #global driver
    if browser == "chrome":
        print("Launch chrome")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        print("Launch Firefox")
        driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Chrome(EdgeChromiumDriverManager().install())
    else:
        print("provide valid browser")
    option = Options()
    option.add_argument('--disable-notifications')
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='class', autouse =True)
def browser(request):
    return request.config.getoption("--browser")

    #driver = webdriver.Chrome(executable_path="C:\\Users\\raikoderajendar\\chromedriver.exe", chrome_options=option)
    #driver = webdriver.Edge(executable_path = "C:\\Users\\raikoderajendar\\msedgedriver.exe")
    # driver.get("http://practice.automationtesting.in/")
    # driver.maximize_window()
    # request.cls.driver = driver
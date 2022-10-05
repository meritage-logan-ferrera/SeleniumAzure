#Run Selenium tests in parellel on Selenium Grid using Pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver as appium_webdriver
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service

# @pytest.fixture(params=["firefox", "chrome", "edge"], scope='class')
@pytest.fixture(params=["firefox", "chrome", "edge"])
# @pytest.fixture(params=["firefox", "chrome"])
# @pytest.fixture(params=["firefox"])
# @pytest.fixture()
def init__driver(request):
  
  if request.param == "firefox":
    browser_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=browser_options)
  if request.param == "chrome":
    browser_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=browser_options)
  if request.param == "edge":
    browser_options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=browser_options)
  
  browser_options.add_argument('--headless')
  
  # driver.implicitly_wait(10)
  driver.set_window_position(0,0)
  driver.set_window_size(1920,1080)
  request.cls.driver = driver
  yield
  driver.close()
  driver.quit()
  print("Test Completed")
  driver = None

  

# @pytest.fixture(scope="class")
# def driver_android_init(request):
#   url = "http://localhost:4444/wd/hub"
  
#   appium_options = UiAutomator2Options()
#   appium_options.platform_name = "Android"
#   appium_options.device_name = "emulator-5556"
#   appium_options.automation_name = "UIAutomator2"
#   appium_options.avd = "Nexus_5_API_30"
#   appium_options.new_command_timeout = "200"
#   appium_options.set_capability("browserName", "Chrome")
#   web_driver = appium_webdriver.Remote(
#     url, 
#     options=appium_options
#   )
#   request.cls.driver = web_driver
#   yield
#   web_driver.quit()

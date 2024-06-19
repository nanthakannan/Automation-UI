import os
import allure
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from allure_commons.types import AttachmentType
import configparser
import logging
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Env:
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)

    # Function to take screenshot
    @staticmethod
    def take_screenshot(driver, name):
        try:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
            driver.save_screenshot(screenshot_path)
            allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
        except WebDriverException:
            print("Failed to take screenshot")

    # Function to initialize WebDriver
    @staticmethod
    def get_driver():
        config = configparser.ConfigParser()
        config.read('.env')
        browser = config['MyData']['Browser']
        url = config['MyData']['URL']
        if browser == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            options = ChromeOptions()
            options.add_argument("--start-maximized")  # Maximize window
            options.add_argument("--disable-notifications")  # Disable notifications
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            options = FirefoxOptions()
            options.add_argument("--start-maximized")  # Maximize window
            options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise Exception("Unsupported browser specified in .env file")
        driver.get(url)
        return driver

def before_scenario(context, scenario):
    context.driver = Env.get_driver()
    context.env = dict(os.environ)

def after_scenario(context, scenario):
    if hasattr(context, 'env'):
        del context.env
    try:
        if scenario.status == "failed":
            Env.take_screenshot(context.driver, scenario.name)
    finally:
        try:
            context.driver.quit()
        except NoSuchWindowException:
            print("Browser window already closed.")
        except WebDriverException:
            print("Error while quitting the browser.")

def before_step(context, step):
    pass

def after_step(context, step):
    pass

def before_all(context):
    pass

def after_all(context):
    pass

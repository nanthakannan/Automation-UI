# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# def get_driver():
#     browser = os.getenv('BROWSER')
#     url = os.getenv('URL')  # Get URL from .env
#     if browser == 'chrome':
#         service = ChromeService(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service)
#     elif browser == 'firefox':
#         service = FirefoxService(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service)
#     else:
#         raise Exception("Unsupported browser specified in .env file")

#     driver.get(url)  # Navigate to the specified URL
#     return driver

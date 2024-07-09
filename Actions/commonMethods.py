from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.booking_page import BookingPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging

class CommonActions:
    
    def __init__(self, driver):
        """
        The above function is a Python constructor that initializes an object with a driver attribute.
        
        :param driver: The `__init__` method is a special method in Python classes used for initializing
        new objects. In the code snippet you provided, the `__init__` method takes two parameters:
        `self` and `driver`
        """
        self.driver = driver
        
def click_new_button(self, locator):
    """
    The function `click_new_button` attempts to locate and click a button element on a web page, logging
    success or specific errors encountered during the process.
    
    :param locator: The `locator` parameter in the `click_new_button` method is used to specify the
    location of the button element that you want to click on. It typically contains information such as
    the type of locator (e.g., CSS selector, XPath), and the value that uniquely identifies the button
    element on the
    """
    try:
            button_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator),
                EC.element_to_be_clickable(locator)
            )
            button_field.click()
            logging.info(f"clicked successfully: {locator}")
    except TimeoutException:
            logging.error("Timed out waiting for the input field to become visible.")
            raise
    except NoSuchElementException:
            logging.error("Input field not found on the page.")
            raise
    except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise 
        
def send_keys_to_input(self, locator, keys):
    """
    The function `send_keys_to_input` sends keys to a specified input field on a web page after clearing
    the field, handling various exceptions that may occur.
    
    :param locator: The `locator` parameter in the `send_keys_to_input` method is used to specify the
    location of the input field on the web page where you want to send keys. It typically consists of a
    tuple that contains a locating strategy (such as CSS selector, XPath, etc.) and the value of
    :param keys: The `keys` parameter in the `send_keys_to_input` function represents the text or keys
    that you want to input into the specified input field on a web page. This could be any string of
    text or a sequence of keys such as special keys like Enter, Tab, or arrow keys. The
    """
    try:
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            input_field.clear()
            input_field.send_keys(keys)
            logging.info(f"Sent keys to input field: {keys}")
    except TimeoutException:
            logging.error("Timed out waiting for the input field to become visible.")
            raise
    except NoSuchElementException:
            logging.error("Input field not found on the page.")
            raise
    except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise
        
def calendar_icon(self, locator):
    """
    The `calendar_icon` function clicks on a calendar icon element on a web page after waiting for it to
    be visible and clickable.
    
    :param locator: The `locator` parameter in the `calendar_icon` method is used to specify the
    location of the calendar icon element on the web page. It is typically a tuple containing a locator
    strategy (such as CSS selector, XPath, etc.) and a locator value that uniquely identifies the
    calendar icon element
    """
    try:
            calendar_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator),
                EC.element_to_be_clickable(locator)
            )
            calendar_field.click()
            logging.info("Calendar icon is clicked successfully")
    except TimeoutException:
            logging.error("Timed out waiting for the input field to become visible.")
            raise
    except NoSuchElementException:
            logging.error("Input field not found on the page.")
            raise
    except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise
        
def bootstrap_dropdown(self, dropdown_locator, list_locator, text):
    """
    This function is used to interact with a Bootstrap dropdown element by clicking on it and selecting
    an item from the dropdown list.
    
    :param dropdown_locator: The `dropdown_locator` parameter refers to the locator of the dropdown
    element on the webpage. This locator is used to identify and interact with the dropdown element
    using a testing framework or automation tool
    :param list_locator: The `list_locator` parameter in the `bootstrap_dropdown` function is used to
    specify the locator for the dropdown list element within the dropdown component. This locator is
    used to identify the dropdown list element on the web page so that the function can interact with
    it, such as selecting an item from the list
    :param text: The `bootstrap_dropdown` function seems to be a method that interacts with a dropdown
    element in a Bootstrap-based web application. The parameters are as follows:
    """
    try:
            dropdown_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(dropdown_locator),
                EC.element_to_be_clickable(dropdown_locator)
            )
            dropdown_field.click()
            logging.info("dropdown_field is clicked successfully")
    except TimeoutException:
            logging.error("Timed out waiting for the input field to become visible.")
            raise
    except NoSuchElementException:
            logging.error("Input field not found on the page.")
            raise
    except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise
        
    try:
            options = WebDriverWait(self.driver, 10).until(
                # EC.visibility_of_element_located(BookingPage.BootSTRAP),
                EC.visibility_of_all_elements_located(list_locator)
                )
            for option in options:
                logging.info(f"Element text is {option.text}")
    # Example action: Clicking each element
    except TimeoutException:
            logging.error("Timed out waiting for the input field to become visible.")
            raise
    except NoSuchElementException:
            logging.error("Input field not found on the page.")
            raise
    except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise
        
    try:
            found = False
            for option in options:
                if option.text == text:
                        ActionChains(self.driver).move_to_element(option).click().perform()
                        logging.info(f"Option '{text}' is selected successfully")
                        found = True
                        break
            if not found:
                    logging.error(f"Option '{text}' not found in the dropdown options.")
                    raise NoSuchElementException(f"Option '{text}' not found.")
    except Exception as e:
                logging.error(f"An unexpected error occurred while selecting the option: {e}")
                raise
            
            
def verify_element_present(self, locator):
    """
    This function verifies the presence of a specified element identified by a locator.
    
    :param locator: The `locator` parameter typically refers to the way in which an element on a web
    page is identified. This can be done using various methods such as XPath, CSS selectors, class
    names, IDs, etc. The `verify_element_present` function is likely used to check if a specific element
    is present
    """
    try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            logging.info(f"Element located: {locator}")
            return True  # Element is present
    except TimeoutException:
            logging.error(f"Timed out waiting for element: {locator}")
            return False  # Element is not present within the timeout
    except NoSuchElementException:
            logging.error(f"Element not found: {locator}")
            return False  # Element is not present because it doesn't exist
    except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise
            
        
    
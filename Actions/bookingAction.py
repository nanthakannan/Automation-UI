from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.booking_page import BookingPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging

class BookingActions:
    
    def __init__(self, driver):
        self.driver = driver
        
    def click_new_button(self, locator):
        try:
            button_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator),
                EC.element_to_be_clickable(locator)
            )
            button_field.click()
            logging.info("clicked successfully.")
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
            
        
    
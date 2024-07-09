from behave import given, when, then
from environment import Env
import logging
import allure
from utils.screenshot import take_screenshot
from Actions.commonMethods import CommonActions
from pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class Steps:

# Configure logging
    logging.basicConfig(level=logging.DEBUG)
    

@given(u'user navigate to URL')
def user_navigate_to_URL(context):
    logging.info("Title of the page: " + context.driver.title)
    # expected_title = "SpiceJet"
    # expected_title = "SpiceJet - Flight Booking for Domestic and International, Cheap Air Tickets"
    actual_title = context.driver.title
    print (actual_title)
    time.sleep(10)
    # Compare the expected title with the actual title using assert
    # try:
    #     assert expected_title == actual_title, f"Title mismatch! Expected: '{expected_title}', Actual: '{actual_title}'"
    # except AssertionError as e:
    #     take_screenshot(context.driver, "example_failure_screenshot")
    #     raise e


@given(u'verify Smart Tech Logo is displayed')
def verify_Smart_Tech_Logo_is_displayed(context):
    try:
        login_logo = CommonActions(context.driver)
        login_logo.verify_element_present(LoginPage.SMART_TECH_LOGO)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on SMART_TECH_LOGO.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: SMART_TECH_LOGO not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise


@when(u'User type Username as "{Username}" and Password as "{Password}"')
def User_type_Username_and_Password(context,Username,Password):
    try:
        username_field = CommonActions(context.driver)
        username_field.send_keys_to_input(LoginPage.USERNAME, Username)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to send keys to Username field.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Username field not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
    try:
        password_field = CommonActions(context.driver)
        password_field.send_keys_to_input(LoginPage.PASSWORD, Password)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to send keys to Password field.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Password field not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise


@when(u'user click on Login')
def user_click_on_Login(context):
    try:
        signin_button = CommonActions(context.driver)
        signin_button.click_new_button(LoginPage.SIGN_IN)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Sign-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Sign-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise


@then(u'Home page should be displayed')
def Home_page_should_be_displayed(context):
    try:
        login_logo = CommonActions(context.driver)
        login_logo.verify_element_present(LoginPage.SMART_TECH_LOGO)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on SMART_TECH_LOGO.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: SMART_TECH_LOGO not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
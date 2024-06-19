from behave import given, when, then
from environment import Env
import logging
import allure
from utils.screenshot import take_screenshot
from Actions.bookingAction import BookingActions
from pages.booking_page import BookingPage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class Steps:

# Configure logging
    logging.basicConfig(level=logging.DEBUG)
    



@given(u'I open the website')
def navigate_to_url(context):
    logging.info("Title of the page: " + context.driver.title)
       # expected_title = "SpiceJet"
    expected_title = "SpiceJet - Flight Booking for Domestic and International, Cheap Air Tickets"
    actual_title = context.driver.title
    print (actual_title)
    # Compare the expected title with the actual title using assert
    try:
        assert expected_title == actual_title, f"Title mismatch! Expected: '{expected_title}', Actual: '{actual_title}'"
    except AssertionError as e:
        take_screenshot(context.driver, "example_failure_screenshot")
        raise e
    
@when(u'I click on Check-IN')
def Click_Button(context):
    try:
        booking_actions = BookingActions(context.driver)
        booking_actions.click_new_button(BookingPage.CHECK_IN)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Check-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Check-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
@then(u'I pass the Email as "{email}"')
def pass_email(context, email):
    try:
        booking_page = BookingActions(context.driver)  # Assuming BookingPage has driver attribute
        booking_page.send_keys_to_input(BookingPage.EMAIL_ID, email)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to send keys to EMAIL_ID field.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: EMAIL_ID field not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
@then(u'I click on Flights')
def click_flights_button(context):
    try:
        booking_actions = BookingActions(context.driver)
        booking_actions.click_new_button(BookingPage.FLIGHTS)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Check-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Check-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
@then(u'I click on Calender Icon')
def click_calender_button(context):
    try:
        booking_actions = BookingActions(context.driver)
        booking_actions.calendar_icon(BookingPage.CALENDAR)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Check-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Check-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
@then(u'I click on Currency Dropdown')
def select_value_from_Dropdown(context):
    try:
        booking_actions = BookingActions(context.driver)
        booking_actions.bootstrap_dropdown(BookingPage.CURRENCY,BookingPage.BootSTRAP,"LKR")
        time.sleep(10)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Check-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Check-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
@then(u'I click on Round Trip')
def click_round_trip_radio_button(context):
    try:
        booking_actions = BookingActions(context.driver)
        booking_actions.click_new_button(BookingPage.ROUND_TRIP)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Check-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Check-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
@then(u'I select Type')
def click_type_button(context):
    try:
        booking_actions = BookingActions(context.driver)
        booking_actions.click_new_button(BookingPage.TYPE)
        time.sleep(5)  # Optional delay for demonstration purposes
    except TimeoutException:
        logging.error("TimeoutException: Timed out waiting to click on Check-IN button.")
        raise
    except NoSuchElementException:
        logging.error("NoSuchElementException: Check-IN button not found.")
        raise
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        raise
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # config = configparser.ConfigParser()
    # config.read('.env')
    # url = config['MyData']['URL']
    # driver = Env.get_driver()  # Pass the browser argument to get_driver
    # context.driver = driver
    # logging.info("This is the URL " + url)
    # try:
    #     context.driver.get(url)
    #     logging.info("Title of the page: " + context.driver.title)
    # except Exception as e:
    #     # Log error
    #     print(f"Failed to open website: {context.url}")
    #     # Attach screenshot if step fails
    #     take_screenshot(context.driver, "Failed_to_open_website")
    #     # Raise the exception to propagate the failure to the test framework
    #     raise e









# # @given(u'I open the website')
# # def step_impl(context):
# #     browser = get_driver()
# #     context.driver = browser
# #     url = os.environ['URL']
# #     logging.info("This is the URL " + url)
# #     try:
# #         context.driver.get(context.url)
# #         logging.info("url opened1")
# #         logging.info ("Title of the page: " + context.driver.title)
# #         logging.info ("Title is printed")
# #     except Exception as e:
# #         # Log error
# #         logging.info(f"Failed to open website: {context.url}")
# #         # Attach screenshot if step fails
# #         take_screenshot(context.driver, "Failed_to_open_website")
# #         # Raise the exception to propagate the failure to the test framework
# #         raise e
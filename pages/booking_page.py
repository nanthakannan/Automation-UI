from selenium.webdriver.common.by import By


class BookingPage:
    ROUND_TRIP = (By.XPATH, "//*[text()='roundtrip']")

    CHECK_IN = (By.XPATH, "//div[text()='check-in']")
    
    EMAIL_ID = (By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input")
    
    RADIO_BUTTON = (By.XPATH, "//div[text() = 'round trip']")
    
    FLIGHTS = (By.XPATH, "//div[text()='Flights']")
    
    CALENDAR = (By.XPATH, "//div[text()='Departure Date']")
    
    CURRENCY = (By.XPATH, "//div[text()='Currency']")
    
    BootSTRAP = (By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[5]/div[2]/div[2]/div[2]/div/div/div")
    
    ROUND_TRIP = (By.XPATH, "//div[text()='round trip']")
    
    TYPE = (By.XPATH, "//div[text()='Armed Forces']")

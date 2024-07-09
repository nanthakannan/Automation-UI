from selenium.webdriver.common.by import By


class LoginPage:
    # SMART_TECH_LOGO = (By.XPATH, "//*[@id=`root`]/div/div/div[1]/div/div[1]/img")
    
    SMART_TECH_LOGO = (By.XPATH, "//img[@alt='logo']")
    USERNAME = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    SIGN_IN = (By.XPATH, "//button[text()='Sign In']")
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_page import LocatorLoginPage
class TestLogin():

    EMAIL_VALID = "admin@admin.com"
    PASSWORD_VALID = "admin10"
    EMAIL_NOT_REGISTERED = "admin@admin.admin"
    PASSWORD_INVALID = "adminadmin10"
    EMAIL_INVALID = "halopakabar"

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://staging-partner-explore.misterb2b.com/login'
        self.driver.get(self.url)

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        email = self.driver.find_element(*LocatorLoginPage.EMAIL).send_keys(self.EMAIL_VALID)
        button_next = self.driver.find_element(*LocatorLoginPage.BUTTON_NEXT).click()
        password = WebDriverWait(self.driver, 30000).until(EC.visibility_of_element_located(LocatorLoginPage.PASSWORD)).send_keys(self.EMAIL_INVALID)

    def test_invalid_email_address(self):
        email = self.driver.find_element(*LocatorLoginPage.EMAIL).send_keys(self.EMAIL_INVALID)
        button_next = self.driver.find_element(*LocatorLoginPage.BUTTON_NEXT).click()
        WebDriverWait(self.driver, 30000).until(EC.visibility_of_element_located(LocatorLoginPage.EMAIL_ERROR))
        assert self.driver.find_element(*LocatorLoginPage.EMAIL_ERROR).text == "That email address isn't correct"

    def test_email_not_registered(self):
        email = self.driver.find_element(*LocatorLoginPage.EMAIL).send_keys(self.EMAIL_NOT_REGISTERED)
        button_next = self.driver.find_element(*LocatorLoginPage.BUTTON_NEXT).click()
        WebDriverWait(self.driver, 30000).until(EC.presence_of_element_located(LocatorLoginPage.TITLE_CARD_UNAUTHORIZED_USER))
        assert self.driver.find_element(*LocatorLoginPage.TITLE_CARD_UNAUTHORIZED_USER).text == "Not Authorized"
        
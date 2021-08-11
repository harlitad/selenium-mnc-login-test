from tests.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.login_page import LocatorLoginPage


class TestLogin(BasePage):

    EMAIL_VALID = "admin@admin.com"
    PASSWORD_VALID = "admin10"
    EMAIL_NOT_REGISTERED = "admin@admin.admin"
    PASSWORD_INVALID = "adminadmin10"
    EMAIL_INVALID = "halopakabar"

    def setup_method(self):
        self.browser = self.initialize()
        self.browser.get(f'{self.browser.base_url}/login')

    def teardown_method(self):
        self.driver.quit()

    def test_valid_login(self):
        email = self.driver.find_element(*LocatorLoginPage.EMAIL)
        email.send_keys(self.EMAIL_VALID)
        button_next = self.driver.find_element(*LocatorLoginPage.BUTTON_NEXT)
        button_next.click()
        password = WebDriverWait(self.driver, 30000).until(EC.visibility_of_element_located(LocatorLoginPage.PASSWORD))
        password.send_keys(self.EMAIL_INVALID)

    def test_invalid_email_address(self):
        email = self.driver.find_element(*LocatorLoginPage.EMAIL)
        email.send_keys(self.EMAIL_INVALID)
        button_next = self.driver.find_element(*LocatorLoginPage.BUTTON_NEXT)
        button_next.click()
        WebDriverWait(self.driver, 30000).until(EC.visibility_of_element_located(LocatorLoginPage.EMAIL_ERROR))
        assert self.driver.find_element(*LocatorLoginPage.EMAIL_ERROR).text == "That email address isn't correct"

    def test_email_not_registered(self):
        email = self.driver.find_element(*LocatorLoginPage.EMAIL)
        email.send_keys(self.EMAIL_NOT_REGISTERED)
        button_next = self.driver.find_element(*LocatorLoginPage.BUTTON_NEXT)
        button_next.click()
        WebDriverWait(self.driver, 30000).until(EC.presence_of_element_located(LocatorLoginPage.TITLE_CARD_UNAUTHORIZED_USER))
        assert self.driver.find_element(*LocatorLoginPage.TITLE_CARD_UNAUTHORIZED_USER).text == "Not Authorized"
    
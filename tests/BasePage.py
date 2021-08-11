from selenium import webdriver

class BasePage:
    """Base class to initialize the base page that will be called from all
    pages"""

    def initialize(self):
        self.driver = webdriver.Chrome()
        self.driver.base_url = 'https://staging-partner-explore.misterb2b.com'
        return self.driver
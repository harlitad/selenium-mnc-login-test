from selenium.webdriver.common.by import By

class LocatorLoginPage:
    EMAIL = (By.ID, "ui-sign-in-email-input")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Next')]")
    PASSWORD = (By.ID, "ui-sign-in-password-input")
    EMAIL_ERROR = (By.CSS_SELECTOR, "p.firebaseui-error.firebaseui-text-input-error.firebaseui-id-email-error")
    TITLE_CARD_UNAUTHORIZED_USER = (By.CSS_SELECTOR, ".mdl-card.mdl-shadow--2dp.firebaseui-container.firebaseui-id-page-unauthorized-user h1")

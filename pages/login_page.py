from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.open_url(self.URL)
        return self

    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        return self.get_text(self.ERROR_CONTAINER)

    def is_login_button_displayed(self):
        return self.is_visible(self.LOGIN_BUTTON)

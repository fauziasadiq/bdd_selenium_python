
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    DASHBOARD = (By.CLASS_NAME, "app_logo")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_dashboard_visible(self):
        actual_text = self.get_text(self.DASHBOARD)
        assert actual_text=="Swag Labs"
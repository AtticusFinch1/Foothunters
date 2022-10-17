from Pages.BasePage import BasePage
from Locators.LoginPage import Login_locators
from Config.config import TestData
import time

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_LOGIN)
        self.driver.maximize_window()
        time.sleep(2)

    def do_login(self, email, password):
        self.do_send_keys(Login_locators.login_input, email)
        self.do_send_keys(Login_locators.password_input, password)
        self.do_click(Login_locators.register_login_button)
    
    def do_logout(self):
        self.do_click(Login_locators.avatar_icon)
        self.do_click(Login_locators.logout_btn)

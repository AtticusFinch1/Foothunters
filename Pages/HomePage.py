from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Locators.HomePage import HomePage_locators
from Actions.HomePage import ActionsHomePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_LOGIN)
        self.driver.maximize_window()

    def valid_notification(self, username):
        ActionsHomePage.send_notification(self, username)
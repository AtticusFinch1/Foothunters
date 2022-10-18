from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Locators.HomePage import HomePage_locators

from dotenv import load_dotenv
import os
import requests
import time

class ActionsHomePage(BasePage):
    def send_notification(self, username):
        time.sleep(2)
        self.driver.get(TestData.BASE_URL + "player/" + username)
        self.do_click(HomePage_locators.like_btn)
        self.do_click(HomePage_locators.follow_btn)
        LoginPage.do_logout(self)
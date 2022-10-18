from Locators.HomePage import HomePage_locators
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Actions.HomePage import ActionsHomePage
from Actions.GeneralActions import generalActions
from Pages.HomePage import HomePage
from Config.config import TestData


from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import json


class Test_HomePage(BaseTest):
    load_dotenv()

    def test_notification(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.do_login(os.getenv('LOGIN_FAN'), os.getenv('PASSWORD'))
        self.homePage.valid_notification(os.getenv('PLAYER_USERNAME'))
        self.loginPage.do_login(
            os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        time.sleep(2)
        # follower_id = generalActions.get_user_id(
        #     self, os.getenv('PLAYER_USERNAME'))
        # fb_session_cookie = (self.driver.get_cookies())
        # fb_cookie = json.dumps(fb_session_cookie[0]["value"])
        # print(fb_cookie)
        # followers_list = generalActions.get_followers_ids(self, fb_cookie)
        # assert follower_id in followers_list

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
import random


class Test_HomePage(BaseTest):
    load_dotenv()

    def test_notification(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.do_login(os.getenv('LOGIN_FAN'), os.getenv('PASSWORD'))
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.homePage.valid_notification(os.getenv('PLAYER_USERNAME'))
        self.loginPage.do_login(
            os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        time.sleep(2)
        self.loginPage.do_logout()
        # follower_id = generalActions.get_user_id(
        #     self, os.getenv('PLAYER_USERNAME'))
        # fb_session_cookie = (self.driver.get_cookies())
        # fb_cookie = json.dumps(fb_session_cookie[0]["value"])
        # print(fb_cookie)
        # followers_list = generalActions.get_followers_ids(self, fb_cookie)
        # assert follower_id in followers_list

    # Search player by username and compare with last name in search results
    def test_search_profile(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.do_login(
            os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        response = generalActions.new_players_all(self)
        random_user = random.choice(list(response.items()))
        random_username = random_user[0]
        random_lastname = random_user[1]
        self.homePage.search_profile(random_username)
        time.sleep(2)
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        try:
            search_name = self.driver.find_elements(
                By.XPATH, "//span[@class='text-h6 q-mt-md text-weight-medium']")
            search_results = search_name[0].text
            print("random_user, ", random_user,
                  "search_results: ", search_results)
            assert random_lastname in search_results
        except:
            print("Search param is not found.")
        self.loginPage.do_logout()

    def test_filter_profile(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.do_login(
            os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.driver.get(TestData.BASE_URL + "players/")
        time.sleep(1)
        position = ActionsHomePage.get_filter_data(self)
        response = len(position)
        BasePage.scroll_down(self, 5)
        self.homePage.filter_in_all_players()
        players_count = self.driver.find_elements(
            By.CSS_SELECTOR, ".q-btn.q-btn-item.non-selectable.no-outline.q-btn--standard.q-btn--rectangle.q-btn--rounded.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--gradient.gradient.q-py-none.q-px-xl.q-my-md")
        print("players count actual", len(players_count))
        print("players count expected", response)
        self.loginPage.do_logout()
        # assert players_count == response

    def test_filter_profile_gender(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.do_login(
            os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.driver.get(TestData.BASE_URL + "players/")
        time.sleep(1)
        response = self.homePage.filter_profile_gender()
        # assert response['players_male'] == response["players_found"][:2]
        self.loginPage.do_logout()

    def test_messenger(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.do_login(os.getenv('LOGIN_FAN'), os.getenv('PASSWORD'))
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.driver.get(TestData.BASE_URL + TestData.USERNAME_PLAYER)
        self.homePage.send_message(TestData.TEST_MESSAGE)
        self.driver.get(TestData.BASE_URL_LOGIN)
        self.loginPage.do_login(
            os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        response = self.homePage.check_message(
            os.getenv('FAN'), TestData.TEST_MESSAGE)
        assert response["receiver"] == os.getenv(
            'FAN') and response["message"] == TestData.TEST_MESSAGE
        self.loginPage.do_logout()

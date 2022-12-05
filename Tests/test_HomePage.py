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

    def test_messenger(self):
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.driver.get(TestData.BASE_URL + 'messenger/lewowi')
        HomePage.send_message(self, TestData.TEST_MESSAGE)
        LoginPage.do_logout(self)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME_FAN, TestData.PASSWORD)
        response = HomePage.check_message(
            self, os.getenv('PLAYER'), TestData.TEST_MESSAGE)
        assert response["receiver"] == os.getenv(
            'PLAYER') and response["message"] == TestData.TEST_MESSAGEE

#     def test_notification(self):
#         BasePage.wait_for_page_load(
#             self, HomePage_locators.precense_of_home_page_el)
#         try:
#             follower_count_before = generalActions.get_followers_count(self, os.getenv('FAN_USERNAME'))
#             HomePage.valid_notification(self, os.getenv('FAN_USERNAME'))
#             follower_count_after = generalActions.get_followers_count(self, os.getenv('FAN_USERNAME'))
#             assert (follower_count_after == follower_count_before + 1 or follower_count_after == follower_count_before - 1)
#         except:
#             print("Something Went Wrong")

#     # Search player by username and compare with last name in search results
#     def test_search_profile(self):
#         BasePage.wait_for_page_load(
#             self, HomePage_locators.precense_of_home_page_el)        
#         response = generalActions.new_players_all(self)
#         random_user = random.choice(list(response.items()))
#         random_username = random_user[0]
#         random_lastname = random_user[1]
#         HomePage.search_profile(self, random_username)
#         time.sleep(2)
#         self.driver.execute_script(
#             "window.scrollTo(0, document.body.scrollHeight)")
#         time.sleep(2)
#         try:
#             search_name = self.driver.find_elements(
#                 By.XPATH, "//span[@class='text-h6 q-mt-md text-weight-medium']")
#             search_results = search_name[0].text
#             print("random_user, ", random_user,
#                   "search_results: ", search_results)
#             assert random_lastname in search_results
#         except:
#             print("Search param is not found.")

#     def test_filter_profile(self):
#         BasePage.wait_for_page_load(
#             self, HomePage_locators.precense_of_home_page_el)
#         self.driver.get(TestData.BASE_URL + "players/")
#         time.sleep(1)
#         position = ActionsHomePage.get_filter_data(self)
#         response = len(position)
#         BasePage.scroll_down(self, 5)
#         HomePage.filter_in_all_players(self)
#         players_count = self.driver.find_elements(
#             By.CSS_SELECTOR, ".q-btn.q-btn-item.non-selectable.no-outline.q-btn--standard.q-btn--rectangle.q-btn--rounded.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--gradient.gradient.q-py-none.q-px-xl.q-my-md")
#         print("players count actual", len(players_count))
#         print("players count expected", response)
#         # assert players_count == response

#     def test_filter_profile_gender(self):
#         BasePage.wait_for_page_load(
#             self, HomePage_locators.precense_of_home_page_el)
#         self.driver.get(TestData.BASE_URL + "players/")
#         time.sleep(1)
#         response = HomePage.filter_profile_gender(self)
#         # assert response['players_male'] == response["players_found"][:2]



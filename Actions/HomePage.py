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
        self.driver.get(TestData.BASE_URL + 'player/' + username)
        BasePage.do_click(self, HomePage_locators.like_btn)
        BasePage.do_click(self, HomePage_locators.follow_btn)
        LoginPage.do_logout(self)

    def get_filter_data(self):
        client = requests.Session()
        all_players_data = {}
        data_all = []  # get list of objects with id, gender, username
        for i in range(0, 6):
            r = client.post(TestData.BASE_URL + 'api/players/find', data={"page": i + 1, "type": "all"}, verify=False)
            players_all = r.json()["players"]["data"]
            for j in range(len(players_all)):
                id = players_all[j]["id"]
                all_players_data["id"] = id
                username = players_all[j]["profile"]["username"]
                all_players_data["username"] = username
                gender = players_all[j]["profile"]["gender"]
                all_players_data["gender"] = gender
                data_all.append({
                    "id": all_players_data["id"],
                    "username": all_players_data["username"],
                    "gender": all_players_data["gender"]
                })
        return data_all
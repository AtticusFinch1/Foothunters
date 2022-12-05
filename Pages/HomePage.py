from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Locators.HomePage import HomePage_locators
from Actions.HomePage import ActionsHomePage
from collections import Counter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class HomePage(BasePage):

    def valid_notification(self, username):
        ActionsHomePage.send_notification(self, username)

    def search_profile(self, param):
        action = ActionChains(self.driver)
        BasePage.do_click(self, HomePage_locators.search_input)
        BasePage.do_send_keys(self, HomePage_locators.search_input, param)
        action.key_down(Keys.DOWN).key_down(Keys.RETURN).perform()

    def filter_in_all_players(self):
        BasePage.do_click(self, HomePage_locators.filters_new)
        BasePage.scroll_down(self, 5)
        BasePage.do_click(self, HomePage_locators.filters_all)
        BasePage.scroll_down(self, 5)
        players_found = BasePage.do_get_text(self, HomePage_locators.players_found)
        return (players_found)

    def filter_profile_gender(self): # clicks on a random player position and returns position name
        BasePage.do_click(self, HomePage_locators.filter_btn)
        BasePage.do_click(self, HomePage_locators.gender_selector)
        BasePage.do_click(self, HomePage_locators.gender_male)
        BasePage.do_click(self, HomePage_locators.apply_filers)
        time.sleep(1)
        data_all = ActionsHomePage.get_filter_data(self)
        gender_counter = Counter(token["gender"] for token in data_all)
        gender_counter_male = (gender_counter["male"])
        gender_counter_female = (gender_counter["female"])
        players_found = BasePage.get_element_text(self, HomePage_locators.players_found)
        #unique_users = list({v["id"]:v for v in data_all}.values())
        return ({"players_male":gender_counter_male, "players_female":gender_counter_female, "players_found":players_found})

    def send_message(self, message):
        time.sleep(10)
        print(self.driver.current_url)
        BasePage.do_send_keys(self, HomePage_locators.message_input, message)
        BasePage.do_click(self, HomePage_locators.send_button)

    def check_message(self, rec, text_message):
        time.sleep(10)
        self.driver.get(TestData.BASE_URL + 'messenger/')
        receivers_all = BasePage.do_find_elements(self, HomePage_locators.message_receiver)        
        receivers = [el.text for el in receivers_all]
        messages_all = BasePage.do_find_elements(self, HomePage_locators.message_content)
        messages = [message.text for message in messages_all]
        receiver_result = {}
        message_result = {}
        for receiver in receivers:
            if receiver == rec:
                receiver_result["receiver"]=receiver
        for message in messages:
            if message == text_message:
                message_result["message"]=message   
        result = {**receiver_result, **message_result}
        print(result)
        return result

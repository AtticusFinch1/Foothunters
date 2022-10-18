from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Locators.HomePage import HomePage_locators
from Actions.HomePage import ActionsHomePage
from collections import Counter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_LOGIN)
        self.driver.maximize_window()

    def valid_notification(self, username):
        ActionsHomePage.send_notification(self, username)

    def search_profile(self, param):
        action = ActionChains(self.driver)
        self.do_click(HomePage_locators.search_input)
        self.do_send_keys(HomePage_locators.search_input, param)
        action.key_down(Keys.DOWN).key_down(Keys.RETURN).perform()

    def filter_in_all_players(self):
        self.do_click(HomePage_locators.filters_new)
        BasePage.scroll_down(self, 5)
        self.do_click(HomePage_locators.filters_all)
        BasePage.scroll_down(self, 5)
        players_found = self.do_get_text(HomePage_locators.players_found)
        return (players_found)

    def filter_profile_gender(self): # clicks on a random player position and returns position name
        self.do_click(HomePage_locators.filter_btn)
        self.do_click(HomePage_locators.gender_selector)
        self.do_click(HomePage_locators.gender_male)
        self.do_click(HomePage_locators.apply_filers)
        time.sleep(1)
        data_all = ActionsHomePage.get_filter_data(self)
        gender_counter = Counter(token["gender"] for token in data_all)
        gender_counter_male = (gender_counter["male"])
        gender_counter_female = (gender_counter["female"])
        players_found = self.get_element_text(HomePage_locators.players_found)
        #unique_users = list({v["id"]:v for v in data_all}.values())
        return ({"players_male":gender_counter_male, "players_female":gender_counter_female, "players_found":players_found})
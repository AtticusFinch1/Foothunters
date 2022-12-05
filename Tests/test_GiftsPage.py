from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.GiftsPage import GiftsPage
from Pages.BasePage import BasePage
from Locators.HomePage import HomePage_locators
from Actions.GeneralActions import generalActions
from dotenv import load_dotenv
import time
import os

from selenium.webdriver.common.by import By

class Test_GiftsPage(BaseTest):
    load_dotenv()

    def test_get_points(self):
        data = GiftsPage.check_points(self)
        assert data['banner_name'] == 'Oliver Yedemib' and data['banner_points'] == data['card_points']

    def test_get_gifts(self):
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        response = generalActions.get_gifts(self)
        self.driver.get(TestData.BASE_URL + 'gifts/')
        gifts_count = GiftsPage.count_gifts(self)
        get_gifts = generalActions.get_gifts(self)
        assert gifts_count['gifts_total_len'] == get_gifts["gifts_total"]

    def test_outofstock(self):
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.driver.get(TestData.BASE_URL + 'gifts/')
        get_gifts = generalActions.get_gifts(self)
        out_of_stock_id = (get_gifts["gifts_data"]["out_of_stock"])
        gift_cards = GiftsPage.count_gifts(self)
        assert gift_cards['gifts_total'][out_of_stock_id].get_attribute("disabled") == 'true'


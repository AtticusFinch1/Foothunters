from Pages.BasePage import BasePage
from Config.config import TestData
from Locators.GiftsPage import GiftsPage_locators
from Locators.HomePage import HomePage_locators
from Actions.GeneralActions import generalActions
import time

class GiftsPage(BasePage):
    def check_points(self):
        BasePage.wait_for_page_load(
            self, HomePage_locators.precense_of_home_page_el)
        self.driver.get(TestData.BASE_URL + 'gifts/')
        banner_name = BasePage.get_element_text(self, GiftsPage_locators.userCard_username)
        print(banner_name)
        banner_points = BasePage.get_element_text(self, GiftsPage_locators.points_count)
        print(banner_points)
        BasePage.do_click(self, GiftsPage_locators.profile_icon)
        card_points = BasePage.get_element_text(self, GiftsPage_locators.userCard_points)
        data = { 'banner_name':banner_name, 'banner_points':banner_points, 'card_points':card_points }
        return data        
    
    def count_gifts(self):
        gifts_total = BasePage.do_find_elements(self, GiftsPage_locators.gift_card)
        return {'gifts_total_len':len(gifts_total), 'gifts_total':gifts_total}

    

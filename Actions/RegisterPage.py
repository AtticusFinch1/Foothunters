from Pages.BasePage import BasePage
from Config.config import TestData
from Locators.RegisterPage import Register_locators
from dotenv import load_dotenv
import os
import requests
import json

class ActionsPageRegister(BasePage):
    load_dotenv()

    def fill_fan_field(self, username, phone):
        self.do_click(Register_locators.who_am_i)
        self.do_click(Register_locators.role_picker_fun)
        self.do_send_keys(Register_locators.username_input, username)
        self.do_send_keys(Register_locators.phone_input, phone)
        self.do_click(Register_locators.next_fan_finish)
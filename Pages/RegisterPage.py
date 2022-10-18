from Actions.GeneralActions import generalActions
from Actions.RegisterPage import ActionsPageRegister
from Locators.RegisterPage import Register_locators
from Pages.BasePage import BasePage
from Config.config import TestData

import json
import time
import requests
from requests import delete
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_REGISTER)
        self.driver.maximize_window()
        time.sleep(5)
    
    def valid_register_fan(self):
        request = generalActions.create_new_email()
        first_name = request['first_name']
        last_name = request['last_name']
        email = request['email']
        password = request['password']
        re_password = request['password']
        self.do_click(Register_locators.name_input)        
        self.do_send_keys(Register_locators.name_input, first_name)
        self.do_click(Register_locators.surname_input)
        self.do_send_keys(Register_locators.surname_input, last_name)
        self.do_click(Register_locators.email_input)
        self.do_send_keys(Register_locators.email_input, email)
        self.do_click(Register_locators.password_input)
        self.do_send_keys(Register_locators.password_input, password)
        self.do_click(Register_locators.confirm_pass_inp)
        self.do_send_keys(Register_locators.confirm_pass_inp, re_password)
        self.do_click(Register_locators.next_button)
        time.sleep(50)
        inbox = generalActions.get_inbox()
        self.driver.get(inbox[0])
        time.sleep(2)
        ActionsPageRegister.fill_fan_field(self, first_name, '0123456789')



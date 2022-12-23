from Actions.GeneralActions import generalActions
from Actions.RegisterPage import ActionsPageRegister
from Locators.RegisterPage import Register_locators
from Pages.BasePage import BasePage
from Config.config import TestData

import os
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

    def select_role(self, age, role):
        self.do_click(Register_locators.age_picker)
        self.do_click(Register_locators.role_picker_global(age))
        self.do_click(Register_locators.who_am_i)
        self.do_click(Register_locators.role_picker_global(role))

    def valid_register_general(self, first_name, last_name, email, password):
        self.do_click(Register_locators.name_input)        
        self.do_send_keys(Register_locators.name_input, first_name)
        self.do_click(Register_locators.surname_input)
        self.do_send_keys(Register_locators.surname_input, last_name)
        self.do_click(Register_locators.email_input)
        self.do_send_keys(Register_locators.email_input, email)
        self.do_click(Register_locators.password_input)
        self.do_send_keys(Register_locators.password_input, password)
        self.do_click(Register_locators.next_button)
        time.sleep(30)
    
    def delete_account(self):
        self.driver.get(TestData.BASE_URL + "settings/security")
        self.do_click(Register_locators.del_account_btn)
        self.do_send_keys(Register_locators.del_confirm_input, os.getenv("PASSWORD"))
        self.do_click(Register_locators.del_confirm_btn)


    


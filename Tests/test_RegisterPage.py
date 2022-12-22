from Tests.test_base import BaseTest
from Pages.RegisterPage import RegisterPage
from Tests.conftest import TestData
from Pages.BasePage import BasePage
from Pages.GiftsPage import GiftsPage
from Actions.GeneralActions import generalActions
import pytest
import requests
import time
import os

class Test_RegisterPage(BaseTest):
    @pytest.mark.parametrize('age, role, expected', 
    [
        pytest.param('21', 'Manager', '10'),
        pytest.param('23', 'Coach', '10'),
        pytest.param('16', 'Player', '10')
    ])
    def test_valid_register_global(self, age, role, expected):
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.select_role(age, role)
        request = generalActions.create_new_email()
        first_name = request['first_name']
        last_name = request['last_name']
        email = request['email']
        password = os.getenv('PASSWORD')
        self.registerPage.valid_register_general(first_name, last_name, email, password)
        inbox = generalActions.get_inbox()
        self.driver.get(inbox[0])
        time.sleep(2)
        points = GiftsPage.check_points(self)
        assert points["banner_points"] == expected and points["card_points"] == expected
        self.registerPage.delete_account()


    





        
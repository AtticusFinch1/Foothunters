from Tests.test_base import BaseTest
from Pages.RegisterPage import RegisterPage
from Tests.conftest import TestData
from Pages.BasePage import BasePage
from Pages.GiftsPage import GiftsPage
from Actions.GeneralActions import generalActions
from googleApi import GoogleApi
import pytest
import requests
import time
import os

class Test_RegisterPage(BaseTest):
    @pytest.mark.parametrize('age, role, expected', 
    [
        pytest.param('21', 'Manager', '10'),
        pytest.param('23', 'Coach', '10'),
        pytest.param('16', 'Player', '10'),
        pytest.param('22', 'CEO', '10'),
        pytest.param('22', 'Agent', '10'),
    ])
    def test_valid_register_global(self, age, role, expected):
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.select_role(age, role)
        request = generalActions.create_new_email()
        first_name = request['first_name']
        last_name = request['last_name']
        email = os.getenv("GOOGLE_MAIL")
        password = os.getenv("PASSWORD")
        self.registerPage.valid_register_general(first_name, last_name, email, password)
        googleapi = GoogleApi()
        service = googleapi.gmail_authenticate()
        results = googleapi.search_messages(service, "FootHunters")
        print(f"Found {len(results)} results.")
        letter = googleapi.read_message(service, results[0])
        print('letter+++++', letter)
        self.driver.get(letter)
        time.sleep(2)
        points = GiftsPage.check_points(self)
        assert points["banner_points"] == expected and points["card_points"] == expected
        self.registerPage.delete_account()

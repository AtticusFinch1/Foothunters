import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData
@pytest.fixture(autouse=True,scope='class')
def init_driver(request): 
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    web_driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver=web_driver
    yield
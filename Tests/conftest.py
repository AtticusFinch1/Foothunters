import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData
from pyvirtualdisplay import Display


@pytest.fixture(autouse=True, scope='class')
def init_driver(request):
    """ display and --headless is used only for github actions """
    display = Display(visible=0, size=(800, 800))
    display.start()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    web_driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = web_driver
    yield

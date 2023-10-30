from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

class TestClass:
    base_url="https://triphelpercompany.azurewebsites.net"

    def setup_class(self):
        self.driver=webdriver.Chrome()

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_load_home_page(self):
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        driver=self.driver
        # to load a given URL in browser window
        driver.get(self.base_url)
        
        # test whether correct URL/ Web Site has been loaded or not
        assert "TripHelper" in driver.title
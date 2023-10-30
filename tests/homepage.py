import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageCases(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url="https://triphelpercompany.azurewebsites.net"

    # --- Pre - Condition ---
    def setUp(self):
        # declare and initialize driver variable
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=options)
        
        # browser should be loaded in maximized window
        self.driver.maximize_window()

        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.driver.implicitly_wait(10)  #10 is in seconds

    # --- Steps ---
    def test_load_home_page(self):
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        driver=self.driver
        # to load a given URL in browser window
        driver.get(self.base_url)
        
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("TripHelper",driver.title)

    # --- Post - Condition ---
    def tearDown(self):
        # to close the browser
        print(f"\n➜  {self.__class__.__name__}")
        self.driver.close()

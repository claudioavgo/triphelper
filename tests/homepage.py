import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageCases(unittest.TestCase):
    base_url="https://triphelpercompany.azurewebsites.net"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    # --- Casos de teste ---
    def test_load_home_page(self):
        
        driver=self.driver
        
        driver.get(self.base_url)
        
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("TripHelper",driver.title)
    
    # --- Final dos casos de teste ---

    def tearDown(self):
        #print(f"\n➜  {self.__class__.__name__}")
        self.driver.close()
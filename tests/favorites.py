import string
import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FavoriteCases(unittest.TestCase):
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

    #@unittest.skip(reason="Test")
    def test_no_fav_on_new_account(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(2)

        # Logando na conta

        # Clicando no botão de login na página principal

        login_btn = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/a/button')

        login_btn.click()

        # Escrevendo usuário e senha

        # Login

        # email_input = driver.find_element(By.XPATH,'//*[@id="exampleInputEmail1"]')
        # email_input.send_keys("a@email.com")
        # psw_input = driver.find_element(By.XPATH,'//*[@id="exampleInputPassword1"]')
        # psw_input.send_keys("1")
    
        # driver.find_element(By.XPATH,'/html/body/form/button').click()


        driver.find_element(By.XPATH, '/html/body/form/div[3]/p/a').click()

        # Criando conta

        alphabet = string.ascii_lowercase
        username = ''.join(random.choice(alphabet) for _ in range(5))
        email = username+"@email.com"
        password = username

        username_input = driver.find_element(By.XPATH,'/html/body/form/div[1]/input')
        username_input.send_keys(username)

        email_input = driver.find_element(By.XPATH,'/html/body/form/div[2]/input')
        email_input.send_keys(email)

        email_input = driver.find_element(By.XPATH,'/html/body/form/div[3]/input')
        email_input.send_keys(password)

        driver.find_element(By.XPATH,'/html/body/form/button').click()


        # Recebendo a quantidade de favoritos na página

        driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/div/div/button').click()
        
        driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/div/div/ul/a[1]/li/button').click()

        favs = driver.find_elements(By.CLASS_NAME,'card')

        self.assertEqual(len(favs), 0)

    # --- Post - Condition ---
    def tearDown(self):
        # to close the browser
        print(f"\n➜  {self.__class__.__name__}")
        self.driver.close()
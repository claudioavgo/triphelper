import random
import string
import time
import unittest

from bin.destination import *
from selenium import webdriver
from selenium.webdriver.common.by import By
class FavoriteCases(unittest.TestCase):
    base_url="http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=options)
        
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        
    # Casos de teste
    # Para skipar um test use isso antes da função -> @unittest.skip(reason="Test")
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

        # Final dos casos de teste

    #@unittest.skip("demonstrating skipping")
    #@unittest.skip(reason="Test")
    def test_fav_new_place_on_new_account(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(2)

        login_btn = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/a/button')
        login_btn.click()

        driver.find_element(By.XPATH, '/html/body/form/div[3]/p/a').click()

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

        random_country = random.choice(paises)

        cities = []

        for i in cidades["data"]:
            if i["country"] == random_country:
                cities = i["cities"]

        background = driver.find_element(By.XPATH, '/html/body')

        countries_box = driver.find_element(By.XPATH, '//*[@id="countrySelect"]')

        countries_box.click()

        countries_box.send_keys(random_country)

        background.click()

        cities_box = driver.find_element(By.XPATH, '//*[@id="countrySelectCity"]')

        cities_box.click()

        cities_box.send_keys(random.choice(cities))

        background.click()

        see_attractions = driver.find_element(By.XPATH, '//*[@id="attBtn"]')

        see_attractions.click()

        fav_action = driver.find_element(By.XPATH, '//*[@id="like"]')

        fav_action.click()

        heart = driver.find_element_by_xpath("//*[@id='like']/svg/g")

        self.assertEqual(heart.get_attribute("fill"), "red")

    #@unittest.skip("demonstrating skipping")
    #@unittest.skip(reason="Test")
    def test_unfav_place_on_new_account(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(2)

        login_btn = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/a/button')
        login_btn.click()

        driver.find_element(By.XPATH, '/html/body/form/div[3]/p/a').click()

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

        random_country = random.choice(paises)

        cities = []

        for i in cidades["data"]:
            if i["country"] == random_country:
                cities = i["cities"]

        background = driver.find_element(By.XPATH, '/html/body')

        countries_box = driver.find_element(By.XPATH, '//*[@id="countrySelect"]')

        countries_box.click()

        countries_box.send_keys(random_country)

        background.click()

        cities_box = driver.find_element(By.XPATH, '//*[@id="countrySelectCity"]')

        cities_box.click()

        cities_box.send_keys(random.choice(cities))

        background.click()

        see_attractions = driver.find_element(By.XPATH, '//*[@id="attBtn"]')

        see_attractions.click()

        fav_action = driver.find_element(By.XPATH, '//*[@id="like"]')
        
        #time.sleep(1)

        fav_action.click()

        #time.sleep(1)

        profile = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/button') 

        profile.click()

        my_places = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/ul/a[1]/li/button')

        my_places.click()

        ####################################
        ####################################
        ####################################

        driver.refresh()

        time.sleep(1)

        favs_prev = driver.find_elements(By.CLASS_NAME,'card')

        unfav_buttons = driver.find_element(By.XPATH, '//*[@id="dislike"]')

        unfav_buttons.click()

        ####################################
        ####################################
        ####################################
        
        favs_next = driver.find_elements(By.CLASS_NAME,'card')

        self.assertLess(len(favs_prev), len(favs_next))

    def tearDown(self):
        self.driver.close()
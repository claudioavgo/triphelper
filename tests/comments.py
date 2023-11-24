import random
import string
import unittest

from bin.destination import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class CommentCases(unittest.TestCase):
    base_url="http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=options)
        
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        
    # Casos de teste
    # Para skipar um test use isso antes da função -> @unittest.skip(reason="Test")
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

    def test_comment_new_place_on_new_account(self):
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

        comment_box = driver.find_element(By.XPATH, '//*[@id="user-input"]')
        comment_box.send_keys("Que belo lugar!")

        share_button = driver.find_element(By.XPATH, '//*[@id="comment-button"]')
        share_button.click()
        
    def tearDown(self):
        self.driver.close()
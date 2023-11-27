from selenium.webdriver.common.by import By
from destination import cidades, paises
from django.test import TestCase
from selenium import webdriver

import string
import random
import time

# Tests here.

class app_health(TestCase):

    def setUp(self):
        self.base_url = "http://localhost:8000"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_load_home_page(self):
        driver = self.driver

        driver.get(self.base_url)

        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("TripHelper", driver.title)

class fav_test(TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_no_fav_on_new_account(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(2)

        # Logando na conta

        # Clicando no botão de login na página principal

        login_btn = driver.find_element(
            By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/a/button')

        login_btn.click()

        driver.find_element(By.XPATH, '/html/body/form/div[3]/p/a').click()

        # Criando conta

        alphabet = string.ascii_lowercase
        username = ''.join(random.choice(alphabet) for _ in range(5))
        email = username+"@email.com"
        password = username

        username_input = driver.find_element(
            By.XPATH, '/html/body/form/div[1]/input')
        username_input.send_keys(username)

        email_input = driver.find_element(
            By.XPATH, '/html/body/form/div[2]/input')
        email_input.send_keys(email)

        email_input = driver.find_element(
            By.XPATH, '/html/body/form/div[3]/input')
        email_input.send_keys(password)

        driver.find_element(By.XPATH, '/html/body/form/button').click()

        # Recebendo a quantidade de favoritos na página

        driver.find_element(
            By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/button').click()

        driver.find_element(
            By.XPATH, '//*[@id="navbarSupportedContent"]/div/div/ul/a[1]/li/button').click()

        favs = driver.find_elements(By.CLASS_NAME, 'card')

        self.assertEqual(len(favs), 0)

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

        heart = driver.find_element(By.XPATH, "//*[@id='like']/svg/g")

        self.assertEqual(heart.get_attribute("fill"), "red")

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

class comment_test(TestCase):

    def setUp(self):
        self.base_url = "http://localhost:8000"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

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

        comments_section = driver.find_element(By.XPATH, '//*[@id="comments-container"]')

        comments = comments_section.find_elements(By.TAG_NAME, 'p')

        comments_treated = []

        for i in comments:
            comments_treated.append(i.text)

        self.assertIn('Que belo lugar!', comments_treated)


class AccessibilityTest(TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_font_up(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            for i in range(1, random.randint(2, 20)):
                login_btn = driver.find_element(
                    By.XPATH, '//*[@id="increase_font"]')
                login_btn.click()
            passou = True
        except:
            passou = False

        self.assertTrue(passou)

    def test_font_down(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            for i in range(1, random.randint(2, 20)):
                login_btn = driver.find_element(
                    By.XPATH, '//*[@id="decrease_font"]')
                login_btn.click()
            passou = True
        except:
            passou = False

        self.assertTrue(passou)

    def test_font_up_down(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            for i in range(1, random.randint(2, 20)):
                driver.find_element(By.XPATH, '//*[@id="increase_font"]').click()

            for i in range(1, random.randint(2, 20)):
                driver.find_element(By.XPATH, '//*[@id="decrease_font"]').click()

            passou = True
        except:
            passou = False
        
        self.assertTrue(passou)

class switch_mode_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_switch_button(self):
        driver = self.driver
        driver.get(self.base_url)

        switch = driver.find_element(By.XPATH, '//*[@id="flexSwitchCheckDefault"]')
        switch.click()

        self.assertTrue(switch.is_enabled())
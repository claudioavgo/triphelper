import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

time.sleep(5)

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/")

time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

from selenium.webdriver.common.action_chains import ActionChains
action = ActionBuilder(driver)
action.pointer_action.move_to_location(1000, 692) 
action.pointer_action.click()
action.perform()

time.sleep(5)

city = driver.find_element(By.XPATH,'//*[@id="countrySelectCity"]')
city.send_keys("Recife")

time.sleep(5)

seeatrc = driver.find_element(By.XPATH,'//*[@id="attBtn"]')
seeatrc.click()

time.sleep(10)

try:
    driver.quit()
except WebDriverException:
    pass
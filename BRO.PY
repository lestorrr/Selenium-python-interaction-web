from selenium import webdriver # imports the selenium webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://p1wwebd08/lmsv2/auth/login")
driver.maximize_window()
driver.refresh()

link = driver.find_element(By.XPATH, "//a[contains(@href, 'files/index.html')]")

if link:
        driver.execute_script("window.open('http://p1wwebd08/lmsv2/auth/login#frmActiveDirectory');")

text_input = driver.find_element(By.ID, "employee")
ActionChains(driver)\
        .click_and_hold()\
        .pause(1)\
        .send_keys_to_element(text_input, "JMOYA")\
        .perform()

text_input = driver.find_element(By.ID, "password")
ActionChains(driver)\
        .click_and_hold()\
        .pause(1)\
        .send_keys_to_element(text_input, "Ciana052497!3")\
        .perform()

# Interact with the file here
driver.close()
# Close the file window


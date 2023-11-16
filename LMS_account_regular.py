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

driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "active_directory"))
)
element.click()

try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sfemployeenumber"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "sfpassword"))
    )
    username_field.send_keys("120313")
    password_field.send_keys("120313071069")
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )


except Exception as e:
    print(f"An exception occurred: {e}")

finally:
    time.sleep(40)
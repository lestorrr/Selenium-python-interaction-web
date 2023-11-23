import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#LINK NA I AUTOMATE AT TEST
driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")
driver.maximize_window()
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.ID, "active_directory"))
)
element.click()
#ADMIN USER AT PASSWORD
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ademployee"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    username_field.send_keys("JMOYA")
    time.sleep(5)
    password_field.send_keys("Ciana052497!3")
    time.sleep(5)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()
finally:
    time.sleep(500)
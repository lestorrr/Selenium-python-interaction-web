from selenium import webdriver
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
    password_field.send_keys("Ciana052497!3")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()
    time.sleep(3)
#LINK PATH NG COURSE NA I CREATE
    driver.get("http://p1wwebd08/lmsv2/course/home")
    time.sleep(3)
#OTW SA VIEWCOURSE EYY
    driver.get("http://p1wwebd08/lmsv2/course/index/readonly")
    time.sleep(3)
    driver.get("http://p1wwebd08/lmsv2/course/view/NzI=/readonly")
    time.sleep(3)
#DESCRIPTION KET ANO
    driver.find_element(By.NAME, "remarks").click()
    driver.find_element(By.ID, "remarks").send_keys("Test_Course101(web-driver)")
    time.sleep(3)
#CLICKING APPROVED HEHEZ
    driver.find_element(By.ID, "btnApprove").click()
    time.sleep(3)
    driver.find_element(By.ID, "btnYes").click()
    time.sleep(3)

finally:
    time.sleep(100)

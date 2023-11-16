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

driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")
driver.maximize_window()

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "active_directory"))
)
element.click()
#admin user at pass
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
    time.sleep(2)
    driver.get("http://p1wwebd08/lmsv2/course/home")
    link = driver.find_elements(By.XPATH, "//a[@href]")
    for link in link:
        if "files" in link.get_attribute("innerHTML"):
            driver.execute_script("window.open('http://p1wwebd08/lmsv2/course/home');")
    submit_button = WebDriverWait(driver, 10).until
    EC.element_to_be_clickable((By.CLASS_NAME, "active"))
    time.sleep(1)
#LINK SA ADD COURSE
    driver.get("http://p1wwebd08/lmsv2/course/add")
#CREATE COURSE EYYYYYY WANANANENG
    driver.find_element(By.NAME, "course_title").click()
    driver.find_element(By.ID, "course_title").send_keys("automated in python")
    time.sleep(2)
    driver.find_element(By.NAME, "course_duration_hrs").click()
    driver.find_element(By.ID, "course_duration_hrs").send_keys(5)
    time.sleep(2)
    driver.find_element(By.NAME, "course_description").click()
    driver.find_element(By.ID, "course_description").send_keys("test on python webdrivers")
    time.sleep(2)
    #driver.find_element(By.CLASS_NAME, "checkmark").click()
    #time.sleep(2)
finally:
    time.sleep(100)

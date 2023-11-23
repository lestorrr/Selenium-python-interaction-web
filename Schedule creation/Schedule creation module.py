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
    password_field.send_keys("Ciana052497!3")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

#LINK PATH NG COURSE NA I CREATE
    driver.get("http://p1wwebd08/lmsv2")
    time.sleep(1)
#OTW SA VIEWCOURSE EYY
    driver.get("http://p1wwebd08/lmsv2/schedule/home")
    time.sleep(1)
    driver.get("http://p1wwebd08/lmsv2/schedule/add")
    time.sleep(1)
#SELECTA COURSE TUNG NU NUNG TUNG TUNUNG
    #dropdown_element = driver.find_element(By.ID, "select2-CourseID-container")
    #dropdown_element.click()
    #option_to_select = driver.find_element(By.XPATH, "//li[@id='select2-CourseID-result-1f5u-11']")
    #option_to_select.click()
    time.sleep(1)
#TIME AND DATE
    driver.find_element(By.ID, "start_date").click()



    time.sleep(100)
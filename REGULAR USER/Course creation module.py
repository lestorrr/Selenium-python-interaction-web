import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#LINK NA I AUTOMATE AT TEST
driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")
driver.maximize_window()
#ADMIN USER AT PASSWORD
try:
    driver.find_element(By.NAME, "employee_number").click()
    driver.find_element(By.ID, "sfemployeenumber").send_keys("120313")
    password_field = driver.find_element(By.ID, "sfpassword")
    password_field.send_keys("120313071069")
    driver.find_element(By.XPATH, "//*[@id='frmLMSAccount']/form/button").click()
    time.sleep(3)

#HOME KABANATAE
    driver.execute_script("window.open('http://p1wwebd08/lmsv2/course/view/MTA=/readonly');")
    submit_button = WebDriverWait(driver, 10).until

finally:
    time.sleep(500)
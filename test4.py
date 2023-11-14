from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
options=option)

driver.get('http://p1wwebd08/lmsv2/auth/login')
driver.execute_script("window.open('http://p1wwebd08/lmsv2/auth/login#frmActiveDirectory');")
driver.executehref="#frmActiveDirectory"
username_field = driver.find_element(by="name", value="employee_number")
password_field = driver.find_element(by="name", value="Password (Employee Number + Birthdate)")

username_field.send_keys("JMOYA")
password_field.send_keys("Ciana052497!3")

driver.maximize_window()

link = driver.find_element(By.XPATH, "//a[@href='http://p1wwebd08/lmsv2/files/index.html']")

if link:
    driver.execute_script("window.open('http://p1wwebd08/lmsv2/auth/login#frmActiveDirectory');")

    username_field = driver.find_element(by="name", value="employee")
    password_field = driver.find_element(by="name", value="Password")

    username_field.send_keys("JMOYA")
    password_field.send_keys("Ciana052497!3")

    driver.execute_script("window.open('http://p1wwebd08/lmsv2/auth/login#frmActiveDirectory');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    link.click()

    # Interact with the file here

    # Close the file window
    driver.close()

    # Switch back to the original window
    driver.switch_to.window(driver.window_handles[0])

    # Close the second window
    driver.close()

    # Continue with the original flow
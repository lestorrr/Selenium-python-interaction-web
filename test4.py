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

option = Options()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
options=option)

driver.get('http://p1wwebd08/lmsv2/auth/login')



element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#active_directory"))
    )
# Assuming you want to click on the found element
element.click()


username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee"))
    )
password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "employee")))

username_field.send_keys("JMOYA")
password_field.send_keys("Ciana052497!3")

    # Interact with the file here

    # Close the file window
driver.close()

    # Switch back to the original window
driver.switch_to.window(driver.window_handles[0])


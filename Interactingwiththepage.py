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


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("http://p1wwebd08/lmsv2/auth/login")


#<input type="text" name="passwd" id="passwd-id" />    👈 ETO LALAGAY EH AYAW PADEN HAHAHA

element = driver.find_element(By.ID, "employee_number")
element = driver.find_element(By.NAME, "employee_number")
element = driver.find_element(By.XPATH, "//input[@id='employee_number']")
element = driver.find_element(By.CSS_SELECTOR, "input#employee_number")


element.send_keys("JMOYA")
element.clear()

time.sleep(20)

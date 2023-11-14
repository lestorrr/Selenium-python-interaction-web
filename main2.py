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


option = Options()
option.add_experimental_option("detach",True)
path_to_chromedriver = r"C:\Users\ATP002311\Documents\chromedriver-win64\chromedriver.exe"
chrome = webdriver.Chrome(executable_path=path_to_chromedriver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
options=option)

driver.get('http://p1wwebd08/lmsv2/auth/login')

def test_login():
    path = "http://p1wwebd08/lmsv2/auth/login"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(path)
    ADaccount = "JMOYA"
    password = "Ciana052497!3"
    time.sleep(5)
    AD=driver.find_element(By.ID,'employee')
    AD.clear()
    time.sleep(2)
    AD.send_keys(ADaccount)
    User=driver.find_element(By.ID,'password')
    User.clear()
    time.sleep(2)
    User.send_keys(password)
    time.sleep(2)
    Login=driver.find_element(By.CLASS_NAME,'btn')
    Login.click()


driver.switch_to.window(driver.window_handles[1])


driver.close()

driver.switch_to.window(driver.window_handles[0])

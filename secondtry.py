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


path_to_chromedriver = r"C:\Users\ATP002311\Documents\chromedriver-win64\chromedriver.exe"
ChromeDriverManager = webdriver.Chrome(executable_path=path_to_chromedriver)
ChromeDriverManager.get('http://p1wwebd08/lmsv2/auth/login')

username_field = ChromeDriverManager.find_element_by_id('employee_number')
password_field = ChromeDriverManager.find_element_by_name('Password (Employee Number + Birthdate)')
submit_button = ChromeDriverManager.find_element_by_xpath("//button[@type='submit']")

username_field.send_keys('JMOYA')
password_field.send_keys('Ciana052497!3')
submit_button.click()




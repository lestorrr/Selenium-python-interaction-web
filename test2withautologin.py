from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

option = Options()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
options=option)

options = Options()
options.binary_location = r"C:Users\ATP002311\Documents\chromedriver-win64chromedriver.exe"
driver = webdriver.Chrome(chrome_options=options)

driver.get("http://p1wwebd08/lmsv2/auth/login")
row_data = driver.find_element(By.XPATH,'//*[@id="active_directory"]')


time.sleep(3)

username_field = driver.find_element(by="name", value="username")
password_field = driver.find_element(by="name", value="password")

username_field.send_keys("120313")
password_field.send_keys("120313071069")

submit_button = driver.find_element(by="name", value="submit")
submit_button.click()

# Switch to the new window
new_window_handle = driver.window_handles[1]
driver.switch_to.window(new_window_handle)

# Interact with the elements in the new window


# For example, you can use the following line to get the page title of the new window
new_window_title = driver.title
print(new_window_title)

original_window_handle = driver.window_handles[0]
driver.switch_to.window(original_window_handle)

time.sleep(5)

driver.quit()
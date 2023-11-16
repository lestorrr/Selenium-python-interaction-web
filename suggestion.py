from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "active_directory"))
)
element.click()

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
            time.sleep(40)
            driver.switch_to.window(driver.window_handles[1])
            link.click()
    for link in link:
            if "link" in link.get_attribute("innerHTML"):
                link = driver.find_elements(By.XPATH, "//a[@href]")
            driver.execute_script("window.open('http://p1wwebd08/lmsv2/course/add');")
            element = driver.find_element(By.CSS_SELECTOR, "input#employee_number")
            link.click()
            time.sleep(40)
finally:
    # Navigate back to the previous page
    time.sleep(40)
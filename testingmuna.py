from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")

try:
    # wait for the username input field to be clickable
    username_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#active_directory"))
    )
    username_input.send_keys("your_username")

    # wait for the password input field to be clickable
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#passwd-id"))
    )
    password_input.send_keys("your_password")

    # wait for the submit button to be clickable
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # perform other actions as needed
finally:
    driver.quit()
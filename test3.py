from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")

try:

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "employee_number"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Password (Employee Number + Birthdate)")))

    username_field.send_keys("JMOYA")
    password_field.send_keys("Ciana052497!3")

    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )

finally:
    driver.quit()
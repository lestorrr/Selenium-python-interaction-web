import self
import driver
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

driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")

def setup_method(cls, method):
        cls.driver = webdriver.Chrome()
        cls.vars = {}


def teardown_method(cls, method):
        cls.driver.quit()

def test_createcourse(cls):
        cls.driver.get("http://p1wwebd08/lmsv2/auth/login")
        cls.driver.set_window_size(1200, 746)

        # Log in
        cls.driver.find_element(By.ID, "active_directory").click()
        cls.driver.find_element(By.ID, "ademployee").click()
        cls.driver.find_element(By.ID, "ademployee").send_keys("JMOYA")
        cls.driver.find_element(By.ID, "adpassword").click()
        cls.driver.find_element(By.ID, "adpassword").send_keys("Ciana052497!3")
        cls.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()

        # Navigate to create course
        cls.driver.find_element(By.CSS_SELECTOR, ".fa-graduation-cap").click()
        cls.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(2) .small-box-footer > .fas").click()
        cls.driver.find_element(By.CSS_SELECTOR, ".w3-list-extend-selected > h2").click()
 
        # Fill in course details
        cls.driver.find_element(By.ID, "course_title").click()
        cls.driver.find_element(By.ID, "course_title").send_keys("Test Course 101")
 
        # Adding explicit wait for the element to be clickable
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "course_duration_hrs")))
 
        # Set course duration
        element = cls.driver.find_element(By.ID, "course_duration_hrs")
        actions = ActionChains(cls.driver)
        actions.double_click(element).perform()
        cls.driver.find_element(By.ID, "course_duration_hrs").send_keys("5")
 
        # Add course description
        cls.driver.find_element(By.ID, "course_description").click()
        cls.driver.find_element(By.ID, "course_description").send_keys("Course creation testing")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) .container:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".row:nth-child(10) .container:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".row:nth-child(15) .container:nth-child(2)").click()
        driver.find_element(By.ID, "btnAddPreview").click()
        driver.find_element(By.CSS_SELECTOR, "#btnAddPreviewSubmit > .fa").click()

        # Switch back to the main frame
        driver.switch_to.default_content()
        
        time.sleep(50)
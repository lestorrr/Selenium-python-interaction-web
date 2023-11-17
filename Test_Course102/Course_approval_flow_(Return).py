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

#LINK NA I AUTOMATE AT TEST
driver = webdriver.Chrome()
driver.get("http://p1wwebd08/lmsv2/auth/login")
driver.maximize_window()
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.ID, "active_directory"))
)
element.click()
#ADMIN USER AT PASSWORD
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
#LINK PATH NG COURSE NA I CREATE
    driver.get("http://p1wwebd08/lmsv2/course/home")
    link = driver.find_elements(By.XPATH, "//a[@href]")
    for link in link:
        if "files" in link.get_attribute("innerHTML"):
            driver.execute_script("window.open('http://p1wwebd08/lmsv2/course/home');")
    submit_button = WebDriverWait(driver, 10).until
    EC.element_to_be_clickable((By.CLASS_NAME, "active"))
    time.sleep(1)
#LINK SA ADD COURSE CODEEEEEEEEEE
    driver.get("http://p1wwebd08/lmsv2/course/add")
#CREATE COURSE CODEEEEEEEEEEEEEEEEE
#TITLE NG COURSE
    driver.find_element(By.NAME, "course_title").click()
    driver.find_element(By.ID, "course_title").send_keys("Test_Course102(webdriver)")
    time.sleep(2)
#DURATION NG COURSE
    driver.find_element(By.NAME, "course_duration_hrs").click()
    driver.find_element(By.ID, "course_duration_hrs").send_keys(5)
    time.sleep(2)
#DESCRIPTION NG COURSE
    driver.find_element(By.NAME, "course_description").click()
    driver.find_element(By.ID, "course_description").send_keys("Course Return to requestor")
    time.sleep(2)
#LALAGYAN LANG PO NG HASHTAG PAG YES PO UNG ISESELECT DEFAULT PO KASI YUNG YES KAYA NO NEED TO CODE
#Is there a pre-requisite course?
    no_element = driver.find_element(By.XPATH, "//label[contains(.,'No')]")
    no_element.click()
    time.sleep(2)
#Is survey required?
    span_element = driver.find_element(By.XPATH, "//form[@id='frmAdd']/div[6]/div/label[2]/span")
    span_element.click()
    time.sleep(1)
#Is exam required?
    span_element = driver.find_element(By.XPATH, "//form[@id='frmAdd']/div[8]/div/label[2]/span")
    span_element.click()
#SUBMITTTTTTT
    driver.find_element(By.ID, "btnAddPreview").click()
    time.sleep(1)
    driver.find_element(By.ID, "btnAddPreviewSubmit").click()
    #LINK PATH NG COURSE NA I CREATE
    driver.get("http://p1wwebd08/lmsv2/course/home")
    time.sleep(1)
#OTW SA VIEWCOURSE EYY
    driver.get("http://p1wwebd08/lmsv2/course/index/readonly")
    time.sleep(1)
    driver.get("http://p1wwebd08/lmsv2/course/view/NzU=/readonly")
    time.sleep(1)
#DESCRIPTION KET ANO
    driver.find_element(By.NAME, "remarks").click()
    driver.find_element(By.ID, "remarks").send_keys("Test_Course101(web-driver)")
    time.sleep(1)
#CLICKING APPROVED HEHEZ
    driver.find_element(By.ID, "btnReturn").click()
    time.sleep(2)
    driver.find_element(By.ID, "btnYes").click()
    time.sleep(1)

finally:
    time.sleep(100)

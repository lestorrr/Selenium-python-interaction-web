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



def test_get_title():
    path = "https://synapsedev.amkor.com/onboarding_system/public/auth/login"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.execute_script("alert('Test 1 Navigate the URL: Execute!')")
    time.sleep(2)
    driver.switch_to.alert.accept()    
    driver.get(path)
    print(driver.title)
    assert "ATP | Onboarding System" in driver.title
    time.sleep(1)
    driver.execute_script("alert('Test login: Passed ')")        
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.close()
def test_get_login_error():
    path = "https://synapsedev.amkor.com/onboarding_system/public/user/index"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(path)
    ADaccounts = "160502"
    passwords = "Aceraspire723"
    ADacc=driver.find_element(By.ID,'employee')
    ADacc.send_keys(ADaccounts)
    Users=driver.find_element(By.ID,'password')
    Users.send_keys(passwords)
    Log=driver.find_element(By.CLASS_NAME,'btn')
    Log.click()
    error = driver.find_element(By.XPATH,"/html/body[@class='bg-dark']/div[@class='bg-full']/div[@class='container-fluid']/div[@class='row']/div[@class='col-xl-7 col-lg-7 col-md-7']/div[@id='pnlLogin']/div[@class='card-body p-0']/div[@class='row']/div[@class='col-lg-12']/div[@class='p-5 ']/div[@class='tab-content']/div[@id='frmAmkorAccount']/form[@class='user mt-4']/div[@class='alert alert-danger']/ul/li")
    assert error.text == 'Applicant does not exist in Record Register an Account!'
    time.sleep(2)
    driver.execute_script("alert('Testing For wrong credential: Passed')")
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.close()
def test_get_login_success():
    path = "https://synapsedev.amkor.com/onboarding_system/public/user/index"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(path)
    ADaccount = "160508"
    password = "Aceraspire723!"
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
    success = driver.find_element(By.XPATH,"/html/body[@id='page-top']/div[@id='wrapper']/div[@id='content-wrapper']/div[@id='content']/div[@class='container-fluid']/h1")
    assert success.text == 'Welcome!'
    time.sleep(2)
    driver.execute_script("alert('Testing For Right credential: Passed')")
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.close()


def test_New_Record():
    path = "https://synapsedev.amkor.com/onboarding_system/public/user/index"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(path)
    ADaccount = "160508"
    password = "Aceraspire723!"
    AD=driver.find_element(By.ID,'employee')
    AD.clear()
    AD.send_keys(ADaccount)
    User=driver.find_element(By.ID,'password')
    User.clear()
    User.send_keys(password)
    Login=driver.find_element(By.CLASS_NAME,'btn')
    Login.click()

    new = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/a[1]')
    new.click()
    new_record = driver.current_url
    assert new_record == 'https://synapsedev.amkor.com/onboarding_system/public/employee/add'
   
def test_system():
    path = "https://synapsedev.amkor.com/onboarding_system/public/user/index"
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(1)
    driver.execute_script("alert('Test 1 login: Execute ')")        
    time.sleep(2)
    driver.switch_to.alert.accept()
    driver.get(path)
    #time.sleep()
    ADaccount = "160508"
    password = "Aceraspire723!"
    AD=driver.find_element(By.ID,'employee')
    AD.clear()
    AD.send_keys(ADaccount)
    User=driver.find_element(By.ID,'password')
    User.clear()
    User.send_keys(password)
    Login=driver.find_element(By.CLASS_NAME,'btn')
    Login.click()
    time.sleep(1)
    driver.execute_script("alert('Test 1 Login: Passed')")        
    time.sleep(2)
    driver.switch_to.alert.accept()


    #test for create new applicant
    time.sleep(1)
    driver.execute_script("alert('Test 2 Create new applicant: Execute')")        
    time.sleep(2)
    driver.switch_to.alert.accept()
    #time.sleep(3)
    new = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/a[1]')
    new.click()
    #time.sleep(3)
    first_name = driver.find_element(By.CSS_SELECTOR,'#first_name')
    first_name.send_keys('Rachel')
    #time.sleep(3)
    middle_name = driver.find_element(By.ID,'middle_name')
    middle_name.send_keys('Maine')
    #time.sleep(3)
    last_name = driver.find_element(By.ID,'last_name')
    last_name.send_keys('Zane')
    #time.sleep(3)
    email_address = driver.find_element(By.ID,'email_address')
    email_address.send_keys('Rachelzane@gmail.com')
    #time.sleep(3)
    sel = Select(driver.find_element(By.ID,'gender'))
    sel.select_by_value("F")
    #time.sleep(1)
    sel.select_by_index(1)
    #time.sleep(3)
    contact_no = driver.find_element(By.XPATH,"(//input[@name='contact_no[]'])[1]")
    contact_no.send_keys('09445566789')
    #time.sleep(3)
    driver.find_element(By.XPATH,"//button[@id='btnAddContact']").click()
    #time.sleep(1)
    tel = Select(driver.find_element(By.XPATH,'(//select[@name="contact_type[]"])[2]'))
    tel.select_by_value("LANDLINE")
    #time.sleep(1)
    tel.select_by_index(1)
   # time.sleep(3)
    contact_no_2 = driver.find_element(By.XPATH,"(//input[@name='contact_no[]'])[2]")
    contact_no_2.send_keys(24445555)
    

    driver.find_element(By.XPATH,"(//input[@id='mr_no'])[1]").send_keys("atp")
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@class='ui-menu-item-wrapper'][normalize-space()='ATPMR0000001824']").click()
     
    r=driver.find_element(By.XPATH,'//input[@name="resume"]')
    r.send_keys("C:\\Users\\160508\\Downloads\\Test Resume.pdf")

    time.sleep(1)
    driver.execute_script("alert('Test 2 Create new applicant: Passed')")        
    time.sleep(2)
    driver.switch_to.alert.accept()
    
    time.sleep(10)
    driver.quit
   
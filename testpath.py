from selenium import webdriver
import pyautogui


path_to_chromedriver = r"C:\Users\ATP002311\Documents\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()


driver.get("http://p1wwebd08/lmsv2/auth/login#frmActiveDirectory")

def input_username():
    # Find the username field
    username_field = pyautogui.locateOnScreen('username_field.png')

    # Click on the username field
    pyautogui.click(username_field)

    # Type the username
    pyautogui.typewrite('my_username')

# Call the input_username() function
input_username()

# Print the title of the website 
print(driver.title)


driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the URL
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Locators and search strategies

#By XPATH
# Amazon logo
driver. find_element(By.XPATH, "//i class[@a-icon a-icon-logo]")

#By ID
# Email field
driver.find_element(By. ID, "ap_email")

#By XPATH
# Continue Button
driver.find_element(By.XPATH, "//input [@id='continue']")

#By XPATH
#Conditions of Use
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#By XPATH
#Privacy Notice
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#By XPATH
#Need Help Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#By ID
#Shop on Amazon Business link
driver.find_element(By.ID, "ab-sign-in-ingress-link")

#By ID
#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")


driver.quit()
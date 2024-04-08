from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#By CSS Selectors

#find Amazon log on registration page
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=ap_frn_logo']")

#Find "Create Account" text on registration page

driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']")

#Find "Your Name" field by ID
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

#Find "Mobile number or Email " field by ID
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

#Find "Password" field by ID
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

#Find Re-Enter Paasword" field by ID
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

#Find "Continue" button
driver.find_element(By.CSS_SELECTOR, "input#continue")

#Find "Conditions of Use" link on the page
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")


#Find "Privacy Policy" link on the page
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Finf "Sign In" button on Amazon Registration page
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?']")

driver(sleep(10))

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
driver.get("https://www.target.com")

# click Sign In button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

#Click SignIn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

sleep(6)

#verify
#“Sign into your Target account” text is shown
expected =  'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
assert expected == actual_text, f"Expected {expected}, got {actual_text}"


#SignIn button is shown to check for element’s presence, no need to assert here)

# MAke sure login button is shown
driver.find_element(By.ID, "'login")
driver. quit()

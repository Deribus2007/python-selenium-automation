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

#By CSS Selector, ID

driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

#By CSS, classes
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute")

#By multiple classes
driver.find_element(By.CSS_SELECTOR, "input.nav-searchbar.nav-progressive-attribute")

driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")

#By CSS selector Id and class combination
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox.nav-input.nav-progressive-attribute")

#By CSS selector, attributes
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox.nav-input.[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']") # Multiple attributes


driver.find_element(By.CSS_SELECTOR, "#select[aria-describedby='searchDropdownDescription']")
#Contains: *=
driver.find_element(By.CSS_SELECTOR, "a[href*='topnav_lang']")


#fron target, contains: *= for a class
driver.find_element(By.CSS_SELECTOR, "h1[class*='StyleHeading']")

#Note. CSS does not support text. for text use XPATH

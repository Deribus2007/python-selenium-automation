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
driver.get('https://www.target.com/')

# enter 'juice' in search field
driver.find_element(By.ID, 'search').send_keys('juices')

#Click Search button
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)

#Verification of product search succesful

actual_results = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

assert 'juices' in actual_results, f'Error!: {actual_results}'

print('Test case passed')

driver(quit()

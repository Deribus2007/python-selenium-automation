from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from webdriver_manager.core import driver

@when('Click on Sign In Icon')
def click_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "span[class*='styles__LinkText']").click()

def click_sign_in_icon(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()


@then("Verify the Sign In form opened")
def verify_sign_in_form(context):
    expected = 'Sign In form opened'
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
    assert expected == actual_text, f"Expected {expected}, got {actual_text}"

    sleep(6)


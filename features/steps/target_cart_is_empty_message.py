from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get("https://www.target.com/")


@when('Click on the Cart icon')
def click_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()

@then("Verify message 'Your cart is empty'")
def verify_cart_is_empty(context):
    expected = 'Your cart is empty'
    actual_text=context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']")
    assert expected == actual_text, f"Expected {expected}, got {actual_text}"

    sleep(6)

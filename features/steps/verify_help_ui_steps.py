from behave import given, then
from selenium.webdriver.common.by import By

# Define locators
TARGET_HELP_TEXT = (By.XPATH, "//h1[contains(text(),'Target Help')]")
SEARCH_HELP_WINDOW = (By.ID, "query")
SEARCH_ICON = (By.CLASS_NAME, "SearchIcon")
WHAT_WOULD_YOU_LIKE_TO_DO_BOX = (By.XPATH, "//h2[contains(text(),'What would you like to do?')]")
CONTACT_US_BOX = (By.XPATH, "//h2[contains(text(),'Contact us')]")
BROWSE_ALL_HELP_PAGES_LINK = (By.XPATH, "//a[contains(text(),'Browse all Help pages')]")

@given('I am on the Target Help page')
def step_impl(context):
    # Navigate to the Target Help page
    context.driver.get("https://help.target.com/help")

@then('I should see "{element_text}" text')
def step_impl(context, element_text):
    # Verify the presence of the specified text
    element = context.driver.find_element(By.XPATH, f"//*[contains(text(), '{element_text}')]")
    assert element.is_displayed(), f"{element_text} text is not present"

@then('I should see the search help window')
def step_impl(context):
    # Verify the presence of the search help window
    assert context.driver.find_element(*SEARCH_HELP_WINDOW).is_displayed(), "Search help window is not present"

@then('I should see the search icon')
def step_impl(context):
    # Verify the presence of the search icon
    assert context.driver.find_element(*SEARCH_ICON).is_displayed(), "Search icon is not present"

@then('I should see the box "{box_text}"')
def step_impl(context, box_text):
    # Verify the presence of the specified box text
    element = context.driver.find_element(By.XPATH, f"//div[contains(@class, 'Box') and contains(text(), '{box_text}')]")
    assert element.is_displayed(), f"{box_text} box is not present"

@then('I should see the link "{link_text}"')
def step_impl(context, link_text):
    # Verify the presence of the specified link text
    element = context.driver.find_element(By.XPATH, f"//a[contains(text(), '{link_text}')]")
    assert element.is_displayed(), f"{link_text} link is not present"

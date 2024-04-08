from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Define locators
BENEFIT_BOXES = (By.CSS_SELECTOR, ".CircleBenefitItem")


# @given('I am on the Target website')
# def step_impl(context):
#     # Navigate to the Target website
#     context.driver.get("https://www.target.com/")


# @given('I am on the Target Circle page')
# def step_impl(context):
#     # Navigate to the Target Circle page
#     context.driver.get("https://www.target.com/circle")


@then('I should see 6 benefit boxes')
def step_impl(context):
    # Wait for the benefit boxes to load
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(BENEFIT_BOXES))

    # Get the list of benefit boxes
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)

    # Verify that there are 6 benefit boxes
    assert len(benefit_boxes) == 6, "Expected 6 benefit boxes, but found {}".format(len(benefit_boxes))

from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Define locators
BENEFIT_BOXES = (By.CSS_SELECTOR, "div[class*='cell-item-content']")


@given('I am on the Target Circle page')
def target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('I should see 10 benefit boxes')
def see_six_boxes_present(context):
    # Wait for the benefit boxes to load
   # WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(BENEFIT_BOXES))

    # Get the list of benefit boxes
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)

    # Verify that there are 10 benefit boxes
    assert len(benefit_boxes) == 10, "Expected 10 benefit boxes, but found {}".format(len(benefit_boxes))



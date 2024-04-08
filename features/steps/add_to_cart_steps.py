from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Define locators
PRODUCT = (By.CSS_SELECTOR, ".product")
CART_ICON = (By.ID, "nav-cart-count")


@when('I add a product to the cart')
def add_product_to_cart(context):
    # Find and click on a product to add to the cart
    product = context.driver.find_element(*PRODUCT)
    product.click()

    # Wait for the cart icon to update (indicating the product is added)
    WebDriverWait(context.driver, 10).until(EC.text_to_be_present_in_element(CART_ICON, "1"))


@then('I should see the product in the cart')
def see_product_in_cart(context):
    # Verify that the cart contains the added product
    cart_count = int(context.driver.find_element(*CART_ICON).text)
    assert cart_count == 1, "Expected 1 item in the cart, but found {}".format(cart_count)

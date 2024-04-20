from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[data-test='resultsHeading']")
SEARCH_INPUT = (By.ID, "search")


@given('I am on the Target website')
def on_target_website(context):
    # context.driver.get("https://www.target.com")
    context.app.main_page.open_main()

@when('I search for {expected_item}')
def search_for_item(context, expected_item):
    context.app.search_results_page.verify_search_results(expected_item)

@then('I verify that every product has a name and an image')
def verify_product_name_info(context):


    products_image = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="@web/ProductCard/ProductCardImage/primary"] img')
    products_names = context.driver.find_elements(By.CSS_SELECTOR, "a[data-test*='product-title']")

    assert len(products_names) == len(products_image), f"Number of product names is {products_names} and images is {products_image} the result do not match"
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Define locators
SEARCH_INPUT = (By.ID, "search")
SEARCH_BUTTON = (By.ID, "searchButton")


@when('I enter "{search_term}" in the search bar')
def search_term(context, search_term):
    # Enter the search term into the search input
    search_input = context.driver.find_element(*SEARCH_INPUT)
    search_input.clear()
    search_input.send_keys(search_term)


@when('I click the Search button')
def search_button(context):
    # Click the Search button
    search_button = context.driver.find_element(*SEARCH_BUTTON)
    search_button.click()


@then('I should see search results for "{search_term}"')
def step_impl(context, search_term):
    # Wait for search results to appear
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'results for')]")))

    # Verify that search results match the expected search term
    search_results_header = context.driver.find_element_by_xpath("//h1[contains(text(), 'results for')]").text
    assert search_term.lower() in search_results_header.lower(), f"Expected search results for '{search_term}', but found '{search_results_header}'"

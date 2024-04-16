from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the product page')
def on_product_page(context):
    context.driver.get("https://www.target.com/p/A-91511634")

@when('I select each color option and Verify that color matches')
def select_each_color_option(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []

    # Updated the locator for the color options
    COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")

    #You don't need to use WebDriverWait(context.driver, 10).until you can say context.wait.until
    context.wait.until(
        EC.presence_of_element_located(COLOR_OPTIONS),
        message='Color options not present on the page'
    )

    #No we get here the elements from the color options
    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]

    for color in colors:
        color.click() #This code will click through the color options

        #This is just for us to see what colors are shown on the option

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', 'selected_color')


        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    #This is to verify that the expected colors has the same as the actual colors.
    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
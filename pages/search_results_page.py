from selenium.webdriver.common.by import By
from pages.base_page import Page



class SearchResultsPage(Page):

    SEARCH_RESULT_HEADER = (By. XPATH, "//div[@data-test='resultsHeading']")
    def verify_search_results(self, expected_results):

        actual_results = self.find_element(*self.SEARCH_RESULT_HEADER).text
        assert 'expected_results' in actual_results, f'Error!: {expected_results} != actual_results: {actual_results}'
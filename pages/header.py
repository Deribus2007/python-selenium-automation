from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_INPUT = (By.ID, "search")
    SEARCH_BUTTON = (By.ID, "searchButton")


    def search_product(self, item):
        self.input_text('item' , *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)
        sleep(6)
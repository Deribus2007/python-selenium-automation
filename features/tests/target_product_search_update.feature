# Created by grphx at 4/8/2024

Feature: Perform Target Product Search

  Background:
    Given I am on the Target website

  Scenario: Perform a product search and click the Search button
    Given I enter "$search_term" in the search bar
    When I click the Search button
    Then I should see search results for "$search_term"
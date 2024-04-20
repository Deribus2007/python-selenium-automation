# Created by grphx at 4/15/2024
Feature: Verify search functionality on Target website

  Scenario: Search for tea on Target website
    Given I am on the Target website
    When I search for Juices
    Then I verify that every product has a name and an image
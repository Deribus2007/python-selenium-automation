Feature: Verify Target Help UI Elements

  Background:
    Given I am on the Target Help page

  Scenario: Verify presence of specific UI elements
    Then I should see "Target Help" text
    And I should see the search help window
    And I should see the search icon
    And I should see the box "What would you like to do?"
    And I should see the box "Contact us"
    And I should see the link "Browse all Help pages"
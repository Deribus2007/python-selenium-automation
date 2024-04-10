Feature: Verify Target Help UI Elements



  Scenario: Verify presence of specific UI elements
    Given I am on the Target Circle page
    When I should see "Target Help" text
    When I should see the search help window
    And I should see the search icon
    And I should see the box "What would you like to do?"
    And I should see the box "Contact us"
    Then I should see the link "Browse all Help pages"


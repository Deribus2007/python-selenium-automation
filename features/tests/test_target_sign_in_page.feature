# Created by grphx at 3/31/2024
Feature: User Authentication

  Scenario: Verify a logged out user can navigate to Sign In
    Given Open target.com
    When Click on Sign In Icon
    Then Verify the Sign In form opened
# Created by grphx at 3/31/2024
Feature: Verify cart functionality on target.com

  Scenario: Verify "Your cart is empty" message when cart is empty
    Given Open target.com
    When Click on the Cart icon
    Then Verify message 'Your cart is empty'



# Created by grphx at 4/8/2024
Feature: Add Target Product to Cart



  Scenario: Add a product to cart and verify its presence
    When I add a product to the cart
    Then I should see the product in the cart
Feature: Manage Stock
  https://app.jubelio.com/login

  Scenario: Arrange and Managing Stock Item Amount
    Given User is Already logged in and navigated
    When User search item by SKU code with "HJUEID"
    And User will edit and enter value for managing stock
    Then User will be notify after save the value


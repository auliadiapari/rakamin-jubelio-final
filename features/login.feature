Feature: Login
  https://app.jubelio.com/login

  Scenario: Login with valid credential and redirected to home
    Given User is on Jubelio login page
    When User input  Email with "qa.rakamin.jubelio@gmail.com" and Password with "Jubelio123!"
    And User Click on Login
    Then User will be redirected to homepage
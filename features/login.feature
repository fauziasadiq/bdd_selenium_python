
Feature: Login functionality

  @smoke
  Scenario Outline: Successful login
    Given user navigates to login page
    When user enters username "<username>" and password "<password>"
    Then user should see dashboard

    Examples:
      | username | password  |
      | standard_user    | secret_sauce  |

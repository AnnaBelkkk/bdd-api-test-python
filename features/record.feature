Feature: Records management

  Scenario: Adding a New Item
    Given I am on the records page
    When I add a record: "test record"
    Then the list contains: "test record"

  Scenario: Mark post as completed
    Given I am on the records page
    When I add a record: "cat"
    And I mark the record: "cat" as completed
    Then the record is marked as completed
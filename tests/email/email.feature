Feature: Email

  Scenario: Create Scheduled Email
    Given I am Ilse Humbles
    And I have event named Aggregate Robust Supply-Chains
    And I want to send email on August 01, 2022 17:30PM +0800
    And Email subject is DUMMY_HEADER
    And Email content is DUMMY_CONTENT

    When I create scheduled email

    Then Scheduled email is created
    And The event name is Aggregate Robust Supply-Chains
    And The email subject is DUMMY_HEADER
    And The email content is DUMMY_CONTENT
    And The timestamp is August 01, 2022 17:30PM +0800
    And Created by ihumbles0@blogspot.com


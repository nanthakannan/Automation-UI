Feature: Login OCR-STCRANE

    Trying to Login to STCRANE with valid Username and Password

    Scenario Outline: To check login is successfull with Valid Username and Password
        Given user navigate to URL
        And verify Smart Tech Logo is displayed
        When User type Username as "<Username>" and Password as "<Password>"
        And user click on Login
        Then Home page should be displayed

        Examples:
            | Username | Password |
            | admin    | admin    |
            | admin    | admin    |
Feature: Reddit top post title fetching

  Scenario: Get the top post title from a subreddit
    Given I am connected to Reddit
    When I fetch the top post from subreddit "python"
    Then I should get the title of the top post

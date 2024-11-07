import requests
from behave import given, when, then


# Global variable to store the Reddit response data
response_data = None
top_post_title = None

# Constants
BASE_URL = "https://www.reddit.com/r/{subreddit}/top.json?limit=1"


@given("I am connected to Reddit")
def step_impl(context):
    # This is where you could verify internet connection, or simply assume we can make requests
    print("Connected to Reddit API")


@when('I fetch the top post from subreddit "{subreddit}"')
def step_impl(context, subreddit):
    # Fetch the top post using the Reddit API
    url = BASE_URL.format(subreddit=subreddit)
    headers = {"User-Agent": "python:serenity-example:v1.0 (by u/yourusername)"}
    global response_data, top_post_title
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        top_post = response_data["data"]["children"][0]["data"]
        top_post_title = top_post["title"]
    else:
        raise Exception(
            f"Failed to fetch data from Reddit. Status code: {response.status_code}"
        )


@then("I should get the title of the top post")
def step_impl(context):
    # Check if the title was fetched correctly
    assert top_post_title is not None, "No top post found"
    print(f"Top Post Title: {top_post_title}")
    assert (
        isinstance(top_post_title, str) and len(top_post_title) > 0
    ), "The title is empty"

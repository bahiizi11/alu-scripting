# Reddit API (advanced)

This is my work for the advanced Reddit API project. The goal is to get comfortable with calling an API from Python, reading the JSON that comes back, and following pagination until there is nothing left to fetch. Everything uses the `requests` module and the public Reddit endpoints.

## What I wrote

**0-subs.py**
`number_of_subscribers(subreddit)` returns how many subscribers a subreddit has. If the subreddit doesn't exist, it returns 0.

**1-top_ten.py**
`top_ten(subreddit)` prints the titles of the first 10 hot posts. For an invalid subreddit it prints `None`.

**2-recurse.py**
`recurse(subreddit, hot_list=None, after=None)` collects the titles of every hot post. Reddit sends results in pages, so the function calls itself with the `after` value of each page until there are no more. It returns `None` for an invalid subreddit.

**3-count.py**
`count_words(subreddit, word_list, after=None, counts=None)` goes through all the hot post titles the same recursive way and counts how many times each keyword shows up. The match is case-insensitive and only counts whole words, so `java` does not match `javascript` or `java.`. Results are printed from the highest count to the lowest, and ties are sorted A to Z.

## Things I had to be careful about

- An invalid subreddit makes Reddit redirect to a search page, so every request uses `allow_redirects=False` and anything that isn't a 200 is treated as invalid.
- Reddit rejects requests without a custom User-Agent, so each file sets one.
- In `recurse` I used `hot_list=None` instead of `hot_list=[]`. A list as a default argument is shared between calls and keeps growing, which would give wrong results the second time the function is used.
- The project runs on Python 3.4, so I used `.format()` and no f-strings.

## How to run it

Each task has a small main file like the ones in the project description, for example:

    python3 0-main.py programming
    python3 3-main.py programming 'python java javascript'

You need Python 3 and the `requests` module (`sudo apt install python3-requests` on Ubuntu).

## A note on testing

Reddit blocked my connection when I tried the live API, so I tested the logic with a fake `requests` module that returns made-up pages. That covered valid and invalid subreddits, pagination across several pages, and the keyword counting rules.

import os
import tweepy
import os
import tweepy
import praw  # Add this line at the top of the file

# ... rest of your code ...

def fetch_x_data(query, count=100, silent=False):
    bearer_token = os.environ.get('X_BEARER_TOKEN')
    if not bearer_token:
        raise ValueError("X_BEARER_TOKEN environment variable is not set")

    if not silent:
        print(f"Attempting to fetch {count} tweets with query: {query}")
    client = tweepy.Client(bearer_token=bearer_token)

    posts = []
    try:
        for tweet in tweepy.Paginator(client.search_recent_tweets, 
                                      query=query,
                                      tweet_fields=['created_at', 'author_id'],
                                      max_results=100).flatten(limit=count):
            posts.append({
                'platform': 'X',
                'text': tweet.text,
                'user': tweet.author_id,
                'created_at': tweet.created_at
            })
            if not silent:
                print(f"Fetched tweet: {tweet.text[:50]}...")
    except tweepy.errors.TweepyException as e:
        if not silent:
            print(f"Error fetching posts from X: {e}")

    if not silent:
        print(f"Total tweets fetched: {len(posts)}")
    return posts

def fetch_reddit_data(subreddit_name, limit=100):
    reddit = praw.Reddit(
        client_id=os.environ.get('REDDIT_CLIENT_ID'),
        client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
        user_agent="DatasetGenerator/1.0"
    )

    posts = []
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.hot(limit=limit):
            posts.append({
                'platform': 'Reddit',
                'title': submission.title,
                'text': submission.selftext,
                'author': submission.author.name if submission.author else '[deleted]',
                'created_at': submission.created_utc
            })
    except praw.exceptions.PrawcoreException as e:
        print(f"Error fetching posts from Reddit: {e}")
    return posts
if __name__ == "__main__":
    # This block is for testing purposes
    x_data = fetch_x_data("python", 10)
    reddit_data = fetch_reddit_data("python", 10)
    print(f"Fetched {len(x_data)} X posts and {len(reddit_data)} Reddit posts")
import tweepy
import praw
import os

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

def fetch_reddit_data(subreddit, limit=100):
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    subreddit = reddit.subreddit(subreddit)
    posts = []

    for post in subreddit.hot(limit=limit):
        posts.append({
            'title': post.title,
            'body': post.selftext,
            'score': post.score,
            'url': post.url
        })

    return posts

if __name__ == "__main__":
    # This block is for testing purposes
    x_data = fetch_x_data("python", 10)
    reddit_data = fetch_reddit_data("python", 10)
    print(f"Fetched {len(x_data)} X posts and {len(reddit_data)} Reddit posts")
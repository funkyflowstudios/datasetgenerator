import tweepy
import praw
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_x_data(query, count=100):
    """
    Fetch tweets from X (Twitter) based on a query.

    Args:
        query (str): Search query for tweets.
        count (int): Number of tweets to fetch (max 100 per request). Defaults to 100.

    Returns:
        list: A list of dictionaries containing tweet data.
              Each dictionary includes 'id', 'text', 'user', 'created_at',
              'retweet_count', and 'favorite_count'.
    """
    auth = tweepy.OAuthHandler(
        os.getenv('TWITTER_API_KEY'),
        os.getenv('TWITTER_API_SECRET_KEY')
    )
    auth.set_access_token(
        os.getenv('TWITTER_ACCESS_TOKEN'),
        os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )

    api = tweepy.API(auth)

    tweets = []
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=query, tweet_mode='extended').items(count):
            tweets.append({
                'id': tweet.id,
                'text': tweet.full_text,
                'user': tweet.user.screen_name,
                'created_at': tweet.created_at,
                'retweet_count': tweet.retweet_count,
                'favorite_count': tweet.favorite_count
            })
    except tweepy.TweepError as e:
        print(f"Error fetching tweets: {e}")

    return tweets

def get_reddit_data(subreddit, limit=100):
    """
    Fetch posts from a specified subreddit.

    Args:
        subreddit (str): Name of the subreddit to fetch posts from.
        limit (int): Number of posts to fetch. Defaults to 100.

    Returns:
        list: A list of dictionaries containing Reddit post data.
              Each dictionary includes 'id', 'title', 'text', 'author',
              'created_utc', 'score', and 'num_comments'.
    """
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

    posts = []
    try:
        for post in reddit.subreddit(subreddit).hot(limit=limit):
            posts.append({
                'id': post.id,
                'title': post.title,
                'text': post.selftext,
                'author': post.author.name if post.author else '[deleted]',
                'created_utc': post.created_utc,
                'score': post.score,
                'num_comments': post.num_comments
            })
    except praw.exceptions.PRAWException as e:
        print(f"Error fetching Reddit posts: {e}")

    return posts

# Example usage
if __name__ == "__main__":
    x_data = get_x_data("python programming", 10)
    print(f"Fetched {len(x_data)} tweets")
    for tweet in x_data[:3]:
        print(f"Tweet by {tweet['user']}: {tweet['text'][:100]}...")
        print()

    reddit_data = get_reddit_data("python", 10)
    print(f"Fetched {len(reddit_data)} Reddit posts")
    for post in reddit_data[:3]:
        print(f"Post by {post['author']}: {post['title']}")
        print(f"Content preview: {post['text'][:100]}...")
        print()
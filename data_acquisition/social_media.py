import os

try:
    import tweepy
except ImportError:
    print("Tweepy is not installed. X (formerly Twitter) functionality will be limited.")
    tweepy = None

try:
    import praw
except ImportError:
    print("PRAW is not installed. Reddit functionality will be limited.")
    praw = None

def get_x_data(query, count=100):
    if tweepy is None:
        return "Tweepy is not installed. Unable to fetch X (formerly Twitter) data."

    api_key = os.environ.get('X_API_KEY')
    api_key_secret = os.environ.get('X_API_KEY_SECRET')

    if not api_key or not api_key_secret:
        return "X API credentials not found. Please set the X_API_KEY and X_API_KEY_SECRET environment variables."

    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_key_secret
        )

        tweets = []
        for tweet in tweepy.Paginator(client.search_recent_tweets, 
                                      query=query,
                                      tweet_fields=['created_at', 'public_metrics'],
                                      max_results=100).flatten(limit=count):
            tweets.append({
                'id': tweet.id,
                'text': tweet.text,
                'created_at': tweet.created_at,
                'retweet_count': tweet.public_metrics['retweet_count'],
                'like_count': tweet.public_metrics['like_count']
            })

        return tweets
    except tweepy.TweepError as e:
        return f"X API error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def get_reddit_data(subreddit_name, post_limit=100):
    if praw is None:
        return "PRAW is not installed. Unable to fetch Reddit data."

    client_id = os.environ.get('REDDIT_CLIENT_ID')
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET')
    user_agent = os.environ.get('REDDIT_USER_AGENT', 'DatasetGen Script')

    if not client_id or not client_secret:
        return "Reddit API credentials not found. Please set the REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET environment variables."

    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)

        subreddit = reddit.subreddit(subreddit_name)
        posts = []

        for post in subreddit.hot(limit=post_limit):
            posts.append({
                'id': post.id,
                'title': post.title,
                'text': post.selftext,
                'score': post.score,
                'url': post.url,
                'created_utc': post.created_utc,
                'num_comments': post.num_comments,
                'author': str(post.author)
            })

        return posts
    except praw.exceptions.PRAWException as e:
        return f"Reddit API error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Remove the example usage from this file
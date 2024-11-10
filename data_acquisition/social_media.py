import time
import random

def exponential_backoff(attempt, max_delay=900):  # 900 seconds = 15 minutes
    delay = min((2 ** attempt) + random.random(), max_delay)
    print(f"Rate limit reached. Waiting for {delay:.2f} seconds...")
    time.sleep(delay)
def get_x_data(query, count):
    # ... (previous code remains the same)

    attempt = 0
    while len(all_tweets) < count:
        try:
            tweets = client.search_recent_tweets(query=query, max_results=max_results)
            if not tweets.data:
                break
            all_tweets.extend([tweet.text for tweet in tweets.data])
            time.sleep(2)  # Wait for 2 seconds between requests to avoid rate limiting
        except tweepy.TooManyRequests:
            if attempt < 5:  # Max 5 retries
                exponential_backoff(attempt)
                attempt += 1
            else:
                print("Max retries reached. Stopping.")
                break
        except Exception as e:
            print(f"An error occurred while fetching tweets: {str(e)}")
            break

    return all_tweets[:count]

    # ... (rest of the code remains the same)

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
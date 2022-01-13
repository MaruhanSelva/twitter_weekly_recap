import tweepy  # easier time with the twitter API
import pandas as pd 
import datetime as DT

# get_client() uses the bearer token to use tweepy to be able to use Twitter API
# getClient: None -> Client
def get_client(token):
    client = tweepy.Client(bearer_token = token)
    return client

# get_week_ago() gets the datetime for exactly one week ago from now
# getWeekAgo: None -> datetime 
def get_week_ago():
    today = DT.datetime.now(DT.timezone.utc)
    week_ago = today - DT.timedelta(days=7)
    return week_ago

# get_tweets(user, client) fetches 100 of the user's recent tweets up until exactly a week ago using the Twitter API
# get_tweets: str Client -> Union[dict, requests.Response, Response]
# Requires: user must be a valid Twitter username
#           client must be valid
def get_tweets(user, client):
    week_ago = get_week_ago()
    query = 'from:' + user
    tweet_fields = ['created_at', 'lang', 'source', 'public_metrics',
    'attachments', 'referenced_tweets']
    
    response = client.search_recent_tweets(query=query,tweet_fields = tweet_fields, start_time = week_ago, max_results = 100)
    return response

# extract_value(dictionary, key) extracts the value of a key-value pair in a dictionary based on key
# extract_value: dict str -> Any
# Requires: dict must be valid
#           key must be a valid key in dict
def extract_value(dictionary, key):
    value = dictionary[key]
    return value

# extract_referenced_type(tweet) extracts the type of tweet that is given
# extract_referenced_type: tweet -> str
def extract_referenced_type(tweet):
    referenced_str = tweet.referenced_tweets[0]
    split_str = str(referenced_str).split("type=", 1)
    tweet_type = split_str[1]
    return tweet_type

# tabular_tweets(tweets) converts tweet data into a pandas DataFrame
# tabular_tweets: listof(tweet) -> DataFrame
def tabular_tweets(tweets):
    # account for no activity
    if tweets == None:
        return "no activity"
    tweets_data = []
    for tweet in tweets:
        singular_tweet_data = []
        singular_tweet_data.append(tweet.id)
        singular_tweet_data.append(tweet.text)

        # Length of Tweet
        singular_tweet_data.append(len(tweet.text))
        singular_tweet_data.append(tweet.created_at)
        singular_tweet_data.append(tweet.lang)
        singular_tweet_data.append(tweet.source)
        
        ## Splitting public_metrics in a couple of different substrings
        retweet_count = extract_value(tweet.public_metrics, "retweet_count")
        singular_tweet_data.append(retweet_count)
        
        reply_count = extract_value(tweet.public_metrics, "reply_count")
        singular_tweet_data.append(reply_count)
        
        like_count = extract_value(tweet.public_metrics, "like_count")
        singular_tweet_data.append(like_count)
        
        quote_count = extract_value(tweet.public_metrics, "quote_count")
        singular_tweet_data.append(quote_count)
        
        singular_tweet_data.append(tweet.attachments)
        
        ## tweet referenced becomes a little bit annoying to clean afterwards
        if tweet.referenced_tweets == None:
            singular_tweet_data.append("standalone") 
        else:
            post_style = extract_referenced_type(tweet)
            singular_tweet_data.append(post_style)
        tweets_data.append(singular_tweet_data)
    
    columns = ['tweetID', 'text', 'length', 'created_at', 'lang', 'source', 'retweet_count',
           'reply_count', 'like_count', 'quote_count', 'attachments', 'post_style']
    
    ## Make a pandas DataFrame
    tabular_data = pd.DataFrame(tweets_data, columns = columns)

    return tabular_data
import tweepy  # easier time with the twitter API
import pandas as pd 
from tweepy_fetch import *

# avg_stats(ttable) returns a dataframe with summary of the tweet data
# avg_stats: DataFrame -> DataFrame
def avg_stats(ttable):
    ## Account for no tweets
    if type(ttable) == str:
        return ttable

    summary_data = []
    # mode of post_style as it information on retweets is valuable
    mode_post_styles = ttable['post_style'].mode()[0]
    summary_data.append(mode_post_styles)

    activity_number = ttable.shape[0]
    summary_data.append(activity_number)
    number_of_original_tweets = ttable.query("post_style == 'standalone'").shape[0]
    summary_data.append(number_of_original_tweets)
    number_of_replies = ttable.query("post_style == 'replied_to'").shape[0]
    summary_data.append(number_of_replies)
    number_of_retweets = ttable.query("post_style == 'retweeted'").shape[0]
    summary_data.append(number_of_retweets)
    number_of_quotes = ttable.query("post_style == 'quoted'").shape[0]
    summary_data.append(number_of_quotes)
    mode_source = ttable['source'].mode()[0]
    summary_data.append(mode_source)
    mode_lang = ttable['lang'].mode()[0]
    summary_data.append(mode_lang)

    # filter out retweets as the user did not post those tweets
    og_tweets = ttable.loc[ttable.post_style != 'retweeted']
    
    if og_tweets.shape[0] == 0:
        summary_data.append(0)
        summary_data.append(0)
        summary_data.append(0)
        summary_data.append(0)
        summary_data.append(0)
    else:
        # numerical data
        avg_retweet = og_tweets['retweet_count'].mean()
        summary_data.append(avg_retweet)
        avg_reply = og_tweets['reply_count'].mean()
        summary_data.append(avg_reply)
        avg_like = og_tweets['like_count'].mean()
        summary_data.append(avg_like)
        avg_quote = og_tweets['quote_count'].mean()
        summary_data.append(avg_quote)
        avg_length_tweet = og_tweets['length'].mean()
        summary_data.append(avg_length_tweet)

    rows = ['mode_post_styles', 'mode_source', 'total_activity', 'original tweets', 'replies',
    'retweets', 'quotes', 'mode_lang', 'avg_retweet', 'avg_reply', 'avg_like', 'avg_quote',
    'avg_length_tweet']

    summary_stats = pd.DataFrame(summary_data, rows)

    return summary_stats

# results_to_print(summary_stats) prints summary statistics of tweets
#   when given a DataFrame of summary statistics
# results_to_print: DataFrame -> None
def results_to_print(summary_stats):
    # intro differs based on activity
    if type(summary_stats) == str:
        print("You didn't have any activity on twitter this week.")
        return  
    elif summary_stats[0][1] > 20:
        print("1. Someone has been a busy bee on Twitter this week!")
    else:
        print("1. Welcome to your twitter weekly recap!")
    
    # Quickly go over summary statistics on different lines
    # Tweet Counts/Activity Breakdowns
    if summary_stats[0][2] > 0:
        print("2. This week you tweeted " + str(summary_stats[0][2]) + " times!")
    else:
        print("2. This week, you did not tweet anything")

    if summary_stats[0][3] > 0: 
        print("3. You also replied " + str(summary_stats[0][3]) + " times!")
    else: 
        print("3. You did not reply to anything this week.")

    if summary_stats[0][4] > 0:
        print("4. You loved to share this week and retweeted " + str(summary_stats[0][4]) + " times!")
    else:
        print("4. You did not retweet anything this week.")
    
    if summary_stats[0][5] > 0:
        print("5. You loved to react this week and quote tweeted " + str(summary_stats[0][5]) + " times!")
    else:
        print("5. You did not quote tweet anyone this week.")

    if summary_stats[0][12] > 0:
        print("6. You had so much to say that you said " + str(summary_stats[0][12]) + " characters!")
    else: 
        print("6. You did not tweet any text")
    
    print("7. You most common language was " + str(summary_stats[0][6]) + ".")
    print("8. You tended to use " + str(summary_stats[0][7]) + " to tweet!")
    print("9. You got an average of " + str(summary_stats[0][8]) + " retweets on your posts!")
    print("10. You got an average of " + str(summary_stats[0][9]) + " replies on your posts!")
    print("11. You got an average of " + str(summary_stats[0][10]) + " likes on your posts!")
    print("12. You got an average of " + str(summary_stats[0][11]) + " quote tweets on your posts!")

    print("13. That's it for your recap!")

def weeklyrecap():
    username = input("Enter the name of the user: ")
    token = input("Enter your twitter API bearer token: ")
    client = get_client(token)
    response = get_tweets(username, client)
    tweet_data = tabular_tweets(response.data)
    summary_stats = avg_stats(tweet_data)
    results_to_print(summary_stats)

weeklyrecap()

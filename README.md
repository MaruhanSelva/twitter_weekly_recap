# Twitter Weekly Recap

A simple terminal program to provide basic summary statistics of a user's twitter profile using the Twitter API V2.

Table of Contents
* Overview
* Output
* Tech Stack
* Process
* Limitations
* Next Steps


## Overview
The purpose of this Python application is to give users a quick summary of their twitter activity so that they can get a better feel of their activity. My implementation uses the Twitter API and Tweepy (Python Twitter API wrapper) to fetch tweets of a user. To use the program, you need two things; a twitter user handle and a Twitter API bearer token.

## Output
If a user were to enter their username as well as their bearer token, then they would have an output. Here is an example of an output!

```python
1. Someone has been a busy bee on Twitter this week!
2. This week you tweeted 21 times!
3. You also replied 30 times!
4. You loved to share this week and retweeted 15 times!
5. You loved to react this week and quote tweeted 12 times!
6. You had so much to say that you said 118.3015873015873 characters!
7. You most common language was Twitter for iPhone.
8. You tended to use en to tweet!
9. You got an average of 160.0952380952381 retweets on your posts!
10. You got an average of 97.55555555555556 replies on your posts!
11. You got an average of 6300.349206349207 likes on your posts!
12. You got an average of 20.41269841269841 quote tweets on your posts!
13. That's it for your recap!
```

## Tech Stack
The tech stack used to make this is as follows:
* Python3
* Twitter API V2

More specifically, the packages used to make this project are Tweepy, DateTime and Pandas. 

Tweepy was used primarily to make API calls to the Twiiter API faster to write and more intuitive. 
Datatime was used alongside the Tweepy API in order to define timeframes in order to get around one of the Twitter API's limitations which is covered in the limitations section further.
Pandas was used to help convert the data recieved from the Twitter API into a Pandas DataFrame.

## Process
The general process to make this project is as follows:
* Call the Twitter API using Tweepy in order to create a Client instance
* Use that Client instance and a given username to retrieve 100 of that user's most recent tweets up until a week
* Convert the tweets that are given into a Pandas DataFrame
* Run simple statistical summaries on the different fields from tweet and store it in a separate summary Pandas DataFrame
* Display the summaries in the terminal

The reason Pandas was used to heavily within this project was to streamline the data management process and also prepare for the process to become much larger. Analyzing the data in something like an array would have not been efficient, but by using Pandas, the application is able to also take advantage of NumPy's faster processing speeds. Plus, Pandas has many useful functions to produce summary statistics so it felt like a natural choice.

## Limitations
While this project is powered by the Twitter API, it also provides some limitations to the program. For reference, the Twitter API access level that I have is the Essential Level.

#### 1. Rate Limits
The first limiation is that of rate limits. Rate limits being the most API called you can make within a time frame. For the Twitter API V2 at the essential access level, the rate limits are at 180 recent tweet lookups per 15 minutes per user and 500000 per month total. This of course could become somewhat of a problem if the project were to be scaled up. As for work around, the max tweets that a user can lookup at a given time is 100 tweets. 

#### 2. You need to have a valid bearer token
The second limitation is that of the need for a bearer token. Like many other APIs, the Twitter API needs some sort of API key in order to access the service. However, these keys need to remain a secret. Thus, the work around for this is simply to ask the user for their Twitter API bearer token. While it is not the most efficient way to do this, it is a quick work around.

## Next Steps
For this project, there are a couple of next steps for this project. These range from the actual insights extracted from the tweets to the overall size of the project.
1. Turning this project into a service
* Involves deploying and using some sort of backend service implementation

2. Extracting cooler insight from the tweet data
* Experimenting with sentiment analysis on your tweets to see how positive/negative your week has been
* What time of day you have been posting
* Implementing data visualizations

3. Adding OAuth2
* This will help to increase security for users 

# jngu+tros-thesis

Thesis title: Detection of Appearance-Based Tweets Mentioning U.S. Politicians with fastText and VADER

This repository contains the code for our thesis, which investigates the differences in how female and male politicians are referred to in regard to their physical appearance on Twitter. For this, we propose a new experimental method called Scoring Appearance with FastText (SAFT) that estimate the amount of appearance-based language that is present in a tweet. Additionally, we do an analysis to determine how the sentiment (positive, neutral or negative) is expressed in the tweets.
Based on approx. 3M tweets (5M tweets were retrieved using the Tweepy API. These were preprocessed down to 3M).

Findings:
Female politicians have about 2 percentage points more tweets that contain more appearance-based language than male politicians.
The sentiment analysis is performed on tweets that contain at least 50% appearance-based language (about 200K tweets). For both genders, we see that about 42.8% are neutral, 35% are positive and 22.1% are negative. Comparing on genders, male politicians have a few percentage points more positive tweets than female politicians.

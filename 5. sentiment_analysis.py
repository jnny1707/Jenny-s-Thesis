# Run the out-commented lines first-time
#nltk.download('vader_lexicon')
#!pip install vaderSentiment

import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

pickle = pd.read_pickle('cruz_SAFT_4_improved_0.5.pkl')
df = pd.DataFrame(pickle)
new_filename = ('xxx_sentimented_compound.pkl')

# Do sentiment analysis on a text/tweet
def sentiment_function(text):
    analyzer = SentimentIntensityAnalyzer()
    new_text = analyzer.polarity_scores(text)
    return new_text

# Return the compound score
def compound(sentimented_dict):
    return sentimented_dict.get('compound')

df['sentimented'] = df.text_for_sentiment.apply(lambda x: sentiment_function(x))
df['compound'] = df.sentimented.apply(lambda x: compound(x))
pd.to_pickle(df, new_filename)

import nltk
import pandas as pd
import string
from collections import Counter
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from preprocessing_functions import *
from preprocessing_statistics_functions import *

nltk.download('stopwords')
nltk.download('wordnet')

new_filename = 'all_preprocessed_4.pkl' # This is the name for the exported pickle

pickle = pd.read_pickle('all_3_not_preprocessed.pkl')
df_imported = pd.DataFrame(pickle)

# Remove duplicates
df_no_dub = df_imported.drop_duplicates('text').copy()

# Count whenever a politician is mentioned
# Create new columns and assign them to 0
df_no_dub['Ocasio-Cortez'] = 0
df_no_dub['Greene'] = 0
df_no_dub['Gaetz'] = 0
df_no_dub['Cruz'] = 0
df_no_dub['Harris'] = 0
df_no_dub['Buttigieg'] = 0
df_no_dub['Boebert'] = 0
df_no_dub['Booker'] = 0
# Go through the texts to check if they contain the politicians. If so, the value is set to 1
df_no_dub['Ocasio-Cortez'] = df_no_dub.text.apply(lambda x: count_aoc(x))
df_no_dub['Greene'] = df_no_dub.text.apply(lambda x: count_mtg(x))
df_no_dub['Gaetz'] = df_no_dub.text.apply(lambda x: count_gaetz(x))
df_no_dub['Cruz'] = df_no_dub.text.apply(lambda x: count_cruz(x))
df_no_dub['Harris'] = df_no_dub.text.apply(lambda x: count_harris(x))
df_no_dub['Buttigieg'] = df_no_dub.text.apply(lambda x: count_buttigieg(x))
df_no_dub['Boebert'] = df_no_dub.text.apply(lambda x: count_boebert(x))
df_no_dub['Booker'] = df_no_dub.text.apply(lambda x: count_booker(x))

# Only for statistics
# Create a dataframe that stores the frequency of each politician is mentioned
politician_mentioned = {
    'Politician': ['Ocasio-Cortez', 'Greene', 'Gaetz', 'Cruz', 'Harris', 'Buttigieg', 'Boebert', 'Booker'],
    'Mentioned': [df_no_dub['Ocasio-Cortez'].sum(), df_no_dub['Greene'].sum(), df_no_dub['Gaetz'].sum(), df_no_dub['Cruz'].sum(),
                  df_no_dub['Harris'].sum(), df_no_dub['Buttigieg'].sum(), df_no_dub['Boebert'].sum(),
                  df_no_dub['Booker'].sum()]}
politician_mentioned = pd.DataFrame(politician_mentioned)
politician_mentioned

# The tweets with sums less than 2 are included in a new dataframe
# By creating a new column 'single_mentioned' that is 'True' if that text contains only one politician and 'False' otherwise. The True rows are added to the new dataframe
cols = ['Ocasio-Cortez', 'Greene', 'Gaetz', 'Cruz', 'Harris', 'Buttigieg', 'Boebert', 'Booker']
df_no_dub['sum_of_mentioned'] = df_no_dub[cols].sum(axis=1)

df_no_dub['single_mentioned'] = df_no_dub['sum_of_mentioned'].apply(lambda x: single_mention(x))
df = df_no_dub[df_no_dub['single_mentioned']].copy()

# Exclude Twitter messages
df['not_twitter_message'] = df.text.apply(lambda x: is_not_twitter_messages(x))
df = df[df['not_twitter_message']].copy()

# Preprocessing for Sentiment
df['text_for_sentiment'] = df.text
df.text_for_sentiment = df.text_for_sentiment.apply(lambda x: remove_mentions(x))
df.text_for_sentiment = df.text_for_sentiment.apply(lambda x: remove_url(x))
df.text_for_sentiment = df.text_for_sentiment.apply(lambda x: remove_placeholder(x))
df.text_for_sentiment = df.text_for_sentiment.apply(lambda x: remove_html_ref(x))

# Preprocessing for SAFT
df.text = df.text.str.lower()
df.text = df.text.apply(lambda x: remove_mentions(x))
df.text = df.text.apply(lambda x: remove_url(x))
df.text = df.text.apply(lambda x: remove_placeholder(x))
df.text = df.text.apply(lambda x: remove_html_ref(x))
df.text = df.text.apply(lambda x: remove_non_letter_char(x))
df.text = df.text.apply(lambda x: remove_rep_char(x))
df.text = df.text.apply(lambda x: decontract(x))
df.text = df.text.apply(lambda x: tokenize_text_punct(x)) # NOTE: It uses the nltk.word_tokenize

# Stop Words
stopwords = nltk.corpus.stopwords.words('english')

# Add new words to the nltk list of stopwords here:
new_stopwords = ['let', 'also', 'etc', 'nd', 'cannot', 'would', 'could', 'get', 'yes', 'though', 'repaoc', 'aoc', 'ocasio', 'cortez', 'ocasiocortez', 'alexandria', 'margie', 'marge', 'majorie', 'majorietg', 'cory', 'cbooker', 'lboebert', 'pbuttigieg', 'kharris', 'pete', 'kamala', 'harris', 'greene', 'greenee','boebert', 'buttigieg', 'cruz', 'gaetz', 'lauren', 'ted', 'repmtg', 'mtgreenee', 'mtgreene', 'mtg', 'matthew', 'matt', 'mgaetz', 'repmattgaez', 'mattgaetz', 'senbooker', 'corybooker', 'secretarypete', 'petebuttigieg', 'vp', 'kamalaharris', 'repboebert', 'laurenboebert', 'sentedcruz', 'tedcruz']
stopwords.extend(new_stopwords)

# Remove stopwords
df.text = df.text.apply(lambda x: [word for word in x if word not in (stopwords)])

# Remove additional punctuation (e.g., for emojis)
df.text = df.text.apply(lambda x: remove_punctuation(x))

# Lemmatization
df.text = df.text.apply(lambda x: lemmatize_words(x))

# Remove one and two character words
df.text = df.text.apply(lambda x: remove_one_and_two_char(x))

# Remove singletons
word_counter = Counter()
for word in df.text:
    word_counter.update(word)

singletons = set()
for word, count in word_counter.items():
    if count == 1:
        singletons.add(word)

df.text = df.text.apply(lambda x: [word for word in x if word not in (singletons)])

# A final remove of punctuation (as we experience some extra punctuations)
df.text = df.text.apply(lambda x: remove_punctuation(x))

# Remove redundant columns
df = df.drop(['Ocasio-Cortez', 'Greene', 'Gaetz', 'Cruz', 'Harris', 'Buttigieg', 'Boebert', 'Booker', 'sum_of_mentioned','single_mentioned', 'not_twitter_message'], axis = 1)

# Remove empty tweets
df_export = df[df.text.apply(is_text_empty)].copy()

# Export to pickle
pd.to_pickle(df_export, new_filename)

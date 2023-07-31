import pandas as pd
import pickle
from gensim.models import FastText
from saft_functions import *

pickle = pd.read_pickle('all_preprocessed_4.pkl')
df = pd.DataFrame(pickle)
new_filename = 'XXX_SAFT.pkl' # This is the name for the exported pickle
fast_Text_model = FastText.load("XXX") # Load fastText model

df = df.drop(df.columns[[0,1,2,3,4,5,7,8,9,10,11]], axis=1) # Dropping redundant columns

# Create list of tuples (word/appearance score) from tweet-words
df['tweet_as_list'] = df.text.apply(lambda x: as_list(x))

# Create list of tuples (word/appearance score) from tweet-words, but only for words with appearance score above threshold
df['tweet_as_list_thr'] = df.tweet_as_list.apply(lambda x: as_list_thr(x))

# Assign appearance scores as approach 1
df['as_1'] = df.tweet_as_list.apply(lambda x: as_1_2(x))

# Assign appearance scores as approach 2
df['as_2'] = df.tweet_as_list_thr.apply(lambda x: as_1_2(x))

# Assign appearance scores as approach 3
df['as_3'] = df.tweet_as_list_thr.apply(lambda x: as_3(x))

# Export to pickle
pd.to_pickle(df, new_filename)

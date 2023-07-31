import pandas as pd
from gensim.models import FastText

pickle = pd.read_pickle('all_preprocessed_4.pkl')
df = pd.DataFrame(pickle)
new_filename = 'XXX.pkl' # This is the name for the exported pickle

# FastText Modeling 
fast_Text_model = FastText(df.text,
                          vector_size = 300,
                          window = 5,
                          min_count = 5,
                          sample = 1e-3,
                          workers = 4,
                          sg = 1)

# Save model
fast_Text_model.save("fast_text_model_all")

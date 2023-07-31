import contractions
import nltk
import re
import string
import tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer
from nltk import word_tokenize, pos_tag
from string import punctuation

def remove_mentions(text):
    text = re.sub(r'@\w+', '', text)
    return text

def remove_url(text):
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = re.sub(r"www\.[a-z]?\.?(com)+|[a-z]+\.(com)", '', text)
    return text

def remove_placeholder(text):
    text = re.sub(r'{link}', '', text)
    text = re.sub(r"\[video\]", '', text)
    return text

def remove_html_ref(text):
    text = re.sub(r'&[a-z]+;', '', text)
    return text

def tokenize_text_punct(text):
    result = WordPunctTokenizer().tokenize(text)
    return result

def remove_non_letter_char(text):
    text = re.sub(r"[^a-z\s\(\-:\)\\\/\];='#]", '', text)
    return text

def remove_rep_char(text):
    text = re.sub(r'(.)\1{2,}', r'\1', text)
    return text

def remove_one_and_two_char(tokens):
    return_list = []
    for word in tokens:
        if len(word) > 2:
            return_list.append(word)
    return return_list

def decontract(text):
    expanded_text_list = []
    for word in text.split():
        expanded_text_list.append(contractions.fix(word))
    expanded_text = ' '.join(expanded_text_list)
    return expanded_text

def is_not_twitter_messages(text):
    boolean = True
    if 'account is temporarily unavailable because it violates the Twitter Media Policy' in text:
        boolean = False
    return boolean

punctuation_list = list(string.punctuation)
def remove_punctuation(word_list):
    return [w for w in word_list if w not in punctuation_list]

def lemmatize_words(tokens):
    lemmatizer = WordNetLemmatizer()
    lemma_tokens = []
    for word in tokens:
        word1 = lemmatizer.lemmatize(word)
        word2 = lemmatizer.lemmatize(word1, pos='v')
        lemma_tokens.append(lemmatizer.lemmatize(word2, pos='a'))
    return lemma_tokens

def is_text_empty(text):
    boolean = True
    if text == []:
        boolean = False
    return boolean

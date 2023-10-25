from gensim.models import FastText

# Load fastText model
fast_Text_model = FastText.load('/home/jngu/algorithm_and_sentiment_iteration3/fast_text_model_all_300')

# Variables that are used in the SAFT functions
global appearance_based_words, threshold
appearance_based_words = set()
threshold = 0.5

# Set with appearance-based words
gender = {'boy', 'girl', 'man', 'woman', 'male', 'female', 'trans', 'nonbinary', 'masculine', 'feminine'}

race = {'asian', 'hispanic', 'african', 'caucasian', 'nigger', 'negro'}

color = {'brown', 'white', 'black', 'red', 'blue', 'yellow', 'green', 'color', 'grey', 'light', 'dark', 'nude', 'naked'}

age = {'elderly', 'old', 'young', 'infant', 'baby', 'child', 'kid', 'adolescent', 'adult', 'teenager', 'youthful', 'mature', 'age'}

to_be = {'pretty', 'adorable', 'cute', 'attractive', 'beautiful', 'cute', 'elegant', 'gorgeous', 'graceful', 'handsome', 'lovely', 'ravishing', 'stunning', 'charming', 'striking', 'radiant', 'sophisticated', 'exquisite', 'fashionable', 'trendy', 'stylish', 'classy', 'nice', 'good', 'hot', 'slutty', 'ugly', 'disgust', 'hideous', 'unattractive', 'childish', 'filthy', 'cold', 'cheap'}

body = {'body', 'fat', 'overweight', 'skinny', 'slim', 'tall', 'short', 'atletic', 'chubby', 'slender', 'muscular', 'obese', 'bald', 'blond', 'brunette', 'redhead', 'curly', 'bearded', 'fat', 'petite', 'curvy', 'short', 'weak', 'strong', 'furry', 'hairy', 'flex'}

body_parts = {'hair', 'brow', 'nose', 'ear', 'lip', 'tongue', 'chin', 'breast', 'tit', 'clevage', 'boob', 'nipple', 'stomach', 'arm', 'hand', 'finger', 'nail', 'beard', 'moustache', 'tooth', 'hip', 'waist', 'butt', 'ass', 'skeleton', 'skin', 'booty', 'dick', 'penis', 'cock', 'genital', 'vagina', 'cunt', 'pussy', 'pregnant', 'heel', 'foot'}

sexuality = {'milf', 'dilf', 'sex', 'gay', 'homosexual', 'homo'}

makeup = {'makeup', 'lipstick', 'jewelry', 'dress', 'shirt', 'suit', 'tie', 'belt', 'pants', 'skirt', 'sock', 'shoe', 'accessory', 'glass', 'bikini', 'blazer'}

selected_actions = {'twerk', 'dance', 'shave', 'wax', 'sweat', 'spank', 'look', 'see', 'watch', 'observe'}

appearance_based_words.update(gender)
appearance_based_words.update(race)
appearance_based_words.update(color)
appearance_based_words.update(age)
appearance_based_words.update(to_be)
appearance_based_words.update(body)
appearance_based_words.update(body_parts)
appearance_based_words.update(sexuality)
appearance_based_words.update(makeup)
appearance_based_words.update(selected_actions)

# Max similarity between the tweet-word and the words in the appearance-based set. 
# This function is used in as_list()
def word_as_tuple(word):
    max_word_similarity = 0
    if word in appearance_based_words:
        max_word_similarity = 1.0
        return (word, max_word_similarity)
    else:
        for appear_word in appearance_based_words:
            if max_word_similarity > 0.95:
                return (word, max_word_similarity)
            similarity = fast_Text_model.wv.similarity(appear_word, word)
            if similarity > max_word_similarity:
                max_word_similarity = similarity
        return (word, max_word_similarity)

# Returns a list of tuples (word/appearance score) from list of tokens (tweet-words)
# The function is used in approach 1, 2 and 3
def as_list(list_of_tokens):
    as_list = [word_as_tuple(x) for x in list_of_tokens]
    return as_list

# If a similarity value is less than the threshold the value is set to 0
# This function is used in as_list_thr()
def lowval_to_zero(as_tuple):
    word = as_tuple[0]
    similarity = as_tuple[1]
    if similarity < threshold:
        return (word, 0)
    else:
        return as_tuple
    
# For all tuples in as_list use lowval_to_zero() to set values under threshold to 0
# The function is used in approach 2 and 3
def as_list_thr(as_list):
    as_list_thr = [lowval_to_zero(x) for x in as_list]
    return as_list_thr

# Return the appearance score for a whole tweet from the sum of word appearence scores (similarities)
# The function is used in approach 1 and 2
def as_1_2(as_list):
    def sum_similarities(as_list):
        return sum(j for i, j in as_list)
    appearance_score = sum_similarities(as_list)/len(as_list)
    return appearance_score

# Return the share of words that are over the threshold
# The function is used in approach 3
def as_3(as_list):
    count = 0
    for i, j in as_list:
        if j > threshold:
            count = count+1
    appearance_score = count/len(as_list)
    return appearance_score

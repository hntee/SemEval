from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from utils import to_list, to_vec, get_cosine, to_list_without_stopwords

def word_to_synset(word):
    synsets = wordnet.synsets(word)
    return synsets[0] if synsets else None

def to_syn_vec(text):
    not_none = lambda x: x is not None
    lst = to_list_without_stopwords(text)

    synsets = list(filter(lambda t: t is not None, map(word_to_synset, lst)))

    return to_vec(synsets)

def syn_cosine(text1, text2):
    vec1 = to_syn_vec(text1)
    vec2 = to_syn_vec(text2)
    return get_cosine(vec1, vec2)


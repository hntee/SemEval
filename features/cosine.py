from utils import *

def cosine(text1, text2):
    vec1 = to_vec(to_list(text1))
    vec2 = to_vec(to_list(text2))
    return get_cosine(vec1, vec2)

def cosine_without_stopwords(text1, text2):
    vec1 = to_vec(to_list_without_stopwords(text1))
    vec2 = to_vec(to_list_without_stopwords(text2))
    return get_cosine(vec1, vec2)

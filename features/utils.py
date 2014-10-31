import re, math
from collections import Counter
from nltk.corpus import stopwords

WORD = re.compile(r'\w+')


def to_list(text, f=None):
    words = WORD.findall(text)
    if f:
        words = filter(f, words)
    return words

def to_list_without_stopwords(text):
    not_in_stopwords = lambda x: x.lower() not in stopwords.words('english')
    return to_list(text, not_in_stopwords)
    
def to_vec(lst):
    return Counter(lst)

# code from http://stackoverflow.com/a/15174569/3374402
# params: Counters that contain keys and ocurrence times
# like 
# Counter({'good': 2, 'night': 1})

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
       return 0.0
    else:
       return float(numerator) / denominator
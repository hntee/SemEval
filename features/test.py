from text import *
from utils import *
from cosine import *
from wordnet import *
from levenshtein import *
from lcs import * 

s1 = "But other sources close to the sale said Vivendi was keeping the door open to further bids and hoped to see bidders interested in individual assets team up."

s2 = "But other sources close to the sale said Vivendi was keeping the door open for further bids in the next day or two."


func_list=[syn_cosine,
           cosine,
           cosine_without_stopwords,
           normalized_longest_common_subsequence,
           levenshtein]

def test(s1, s2, func_list):
    print 'The sentences are:'
    print s1, '\n', s2
    for f in func_list:
        print f.__name__,":", f(s1, s2)

def t():
	test(s1, s2, func_list)
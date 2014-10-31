from text import *
from utils import *
from cosine import *
from wordnet import *
from levenshtein import *
from lcs import * 


s1 = "The US army invaded Kabul on May 7th last year, 2010."
s2 = "In May 2010, the troops attempted to invade Kabul."

sentences_list = [(s1, s2),
				  ("The bird is bathing in the sink.", "Birdie is washing itself in the water basin."),
				  ("They flew out of the nest in groups.","They flew into the nest together.")

				 ]

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
	for (s1, s2) in sentences_list:
		test(s1, s2, func_list)



# from sklearn import svm
# Z = [[0, 0, 8,6], [2, 2, 55,6]]
# y = [0.5, 2.5]
# clf = svm.SVR()
# clf.fit(Z, y) 
# clf.predict([[1, 1]])

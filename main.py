from sklearn import svm
from scipy.stats import pearsonr

from text import *
from utils import *
from cosine import *
from wordnet import *
from levenshtein import *
from lcs import * 

def sentences_from_file(filename):
    sentences_list = [line.strip().split("\t") for line in open(filename)]
    return sentences_list

def gs_from_file(filename):
    return [line.strip() for line in open(filename)]

def sentences_features(sentences):
    func_list=[syn_cosine,
           cosine,
           cosine_without_stopwords,
           normalized_longest_common_subsequence,
           levenshtein]

    return [[func(s1, s2) for func in func_list] for [s1, s2] in sentences]


def get_features(s1, s2, func_list):
    return [func(s1, s2) for func in func_list]

def get_SVR(features, result):
    clf = svm.SVR()
    clf.fit(features, result)
    return clf

def get_result(features, SVR):
    return SVR.predict(features)

def run(filename):
    print "filename:", filename
    gs_filename = filename.replace("input","gs")
    s_features = sentences_features(sentences_from_file(filename))
    s_gs = gs_from_file(gs_filename)

    SVR = get_SVR(s_features, s_gs)

    test_filename = filename.replace("train","test-gold")
    test_gs_filename = gs_filename.replace("train","test-gold")

    test_features = sentences_features(sentences_from_file(test_filename))
    test_predict = get_result(test_features, SVR)

    test_gs = [float(x) for x in gs_from_file(test_gs_filename)]

    pearson = pearsonr(test_gs, test_predict)

    print "pearson: ", pearson[0]

def all():

    filenames = ["train/STS.input.MSRpar.txt",
                "train/STS.input.MSRvid.txt",
                "train/STS.input.SMTeuroparl.txt"]

    for f in filenames:
        run(f)

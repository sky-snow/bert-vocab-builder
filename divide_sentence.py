import numpy
from nltk.tokenize import sent_tokenize
import logging
from collections import OrderedDict

paths = r'/Users/aeroland/Documents/BTU/bert_corpus/alloys/1/1.txt'
sentence_list = []
gol_dict = OrderedDict()
with open(paths, 'r+') as f:
    document = f.read()
    sentence_list = sent_tokenize(document)

# with open('./sentenc.txt', 'w+') as f:
#     for item in sentence_list:
#         f.write(item+'\n')

numpy_arr = numpy.array([len(length) for length in sentence_list])
print(numpy_arr)
print(numpy_arr.min())
print(numpy_arr.max())
print(numpy_arr.mean())
print(numpy_arr[numpy_arr <= 128])
print(numpy_arr[numpy_arr > 128])

# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 22:39
# @Author  : wuyan
# @Email   :aerolandX@163.com
# @FileName: divide_sentence.py
# @Function:

from nltk.tokenize import sent_tokenize
from concurrent.futures import ThreadPoolExecutor
from collections import OrderedDict
from collections import defaultdict
from queue import Queue
from pathlib import Path
from typing import Any
from typing import Iterable
from typing import Union
import threading
import numpy
import logging
import time


class txt:
    def __init__(self, name, context):
        self.name: str = name
        self.context: list = context


logging.basicConfig(level=logging.INFO, format='[%(threadName)-9s] %(message)s')
source_path = r'G:\BTU\bert_corpus\bert_corpus'
result_path = r''
paths = [str(x) for x in Path(source_path).glob("**/*.txt")]
print(paths)
gol_dict = OrderedDict()
task_queue = Queue()
result_queue = Queue()
max_workers_number = 10


def divide_document_to_sentence(file_path: str) -> Any:
    with open(file_path, 'r+') as f:
        document = f.read()
        sentence_list = sent_tokenize(document)
        text_item = txt(file_path, sentence_list)
        return text_item


def productor(paths: list) -> None:
    executor = ThreadPoolExecutor(max_workers=max_workers_number)
    for result in executor.map(divide_document_to_sentence(), paths):
        task_queue.put(result)
        logging.info('{} already add the queue'.format(result.name))


def consumer():
    ...


with ThreadPoolExecutor(max_workers=max_workers_number) as task:
    ...


def save_to_new_text(item_dict):
    with open(item_dict[task_queue.get()]):
        ...

def statistic_text_info(text_list: list):
    ...

# paths = r'/Users/aeroland/Documents/BTU/bert_corpus/alloys/1/1.txt'
# sentence_list = []
# with open(paths, 'r+') as f:
#     document = f.read()
#     sentence_list = sent_tokenize(document)

# with open('./sentenc.txt', 'w+') as f:
#     for item in sentence_list:
#         f.write(item+'\n')

# numpy_arr = numpy.array([len(length) for length in sentence_list])
# print(numpy_arr)
# print(numpy_arr.min())
# print(numpy_arr.max())
# print(numpy_arr.mean())
# print(numpy_arr[numpy_arr <= 128])
# print(numpy_arr[numpy_arr > 128])

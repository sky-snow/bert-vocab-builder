# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 21:41
# @Author  : wuyan
# @Email   :aerolandX@163.com
# @FileName: mul_process_test.py
# @Function:


from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import time
import logging
import threading
logging.basicConfig(level=logging.INFO, format='[%(threadName)-9s] %(message)s')

max_workers_number = 3

task_queue = Queue()


def productor(paths: list):
    executor = ThreadPoolExecutor(max_workers=max_workers_number)
    for result in executor.map(get_item, paths):
        task_queue.put(result)
        logging.info('{} already add the queue in {}'.format(result,threading.current_thread().ident))

def consumer(queue:Queue):
    task_list=[]
    while True:
        if queue and queue.not_empty:
            task_list.append(queue.get())
            executor = ThreadPoolExecutor(max_workers=max_workers_number)
            for result in executor.map(get_item,task_list ):
                    logging.info('{} already remove the queue in {}'.format(result,threading.current_thread().ident))

def get_item(name):
    time.sleep(3)
    return name

test_list = [1, 2, 3, 4, 5, 6]
productor(test_list)
consumer(task_queue)

#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os

def clear(path):
    files = os.listdir(path)
    for file in files:
        print('[+]checking: '+ str(file))
        if os.path.isdir(file):
            if not os.listdir(file):
                os.rmdir(file)
        elif os.path.isfile(file):
            if os.path.getsize(file) == 0:
                os.remove(file)
    print('[+] success!')

if __name__ == "__main__":
    path = './'
    clear(path)

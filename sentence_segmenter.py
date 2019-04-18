#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script splits sentences by periods. Useful when preprocessing large text
corpuses for BERT.
'''
import os
from nltk.tokenize import word_tokenize, sent_tokenize

def preprocess():
    # Change read/write directories
    with open("/Users/Your/File/Here", "r") as first, open("/Users/Your/New/File/Here", "w") as last:
        for sent in sent_tokenize(first.read()):
            words = sent_tokenize(sent)
            processed_sentence = [w for w in words]
            print(processed_sentence)
            print(processed_sentence, file=last)
preprocess()

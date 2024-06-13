#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
import re

# Regular expression to match contiguous strings of letters
word_pattern = re.compile(r'[a-zA-Z]+')

for line in sys.stdin: 
    line = line.strip() 
    words = word_pattern.findall(line)
    for word in words:
        print(f'{word.lower()}\t1')

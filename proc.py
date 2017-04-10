#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script find .txt files in ['da', 'de', 'el', 'en', 'es', 'fi', 'it', 'fr', 'nl', 'pt'] directories to process it 
inside /txt directory from http://www.statmt.org/europarl/v7/europarl.tgz and it creates a single file for trainning and evaluation both.

The result will have a shuffle of differents languages sentences between 1 and 20 words lenght like this:

----------------------------------
this is an example of sentences-EN
esto es un ejemplo de frase-ES
c'est un exemple de phrase-FR
----------------------------------

And, the result will have a million differents words per language for trainning, and finally, will have 100.000 differents words per language
for evaluation.
"""

# Imports

import os
from random import shuffle

# Structures

lang_directories = ['da', 'de', 'el', 'en', 'es', 'fi', 'fr', 'it', 'nl', 'pt']

lang_results = {'da':'1 0 0 0 0 0 0 0 0 0', 'de':'0 1 0 0 0 0 0 0 0 0', 'el':'0 0 1 0 0 0 0 0 0 0', 'en':'0 0 0 1 0 0 0 0 0 0', 
'es':'0 0 0 0 1 0 0 0 0 0', 'fi':'0 0 0 0 0 1 0 0 0 0', 'fr':'0 0 0 0 0 0 1 0 0 0', 'it':'0 0 0 0 0 0 0 1 0 0', 'nl':'0 0 0 0 0 0 0 0 1 0', 
'pt':'0 0 0 0 0 0 0 0 0 1'}

lang_num_words = dict() 

lang_dict = dict()

invalid_character = ['-',':',';','<','(','–']
replace_character = ['.',',','"']

# Secondary functions

def filter(line):
    return not any(x in line for x in invalid_character)

def replace(line):
    new_line = ""
    for c in replace_character:
        new_line = line.replace(c,"")
    return new_line

def process_line(lines):
    result = list()
    for line in lines:
        new_line = replace(line)
        if len(new_line) > 0 and filter(line) and line.count(' ') <= 19:
            result.append(new_line)              
    return result
        
"""if "<" not in line: #Remove xml lines
            if "(" not in line: #Remove () lines
                if line.count(' ') <= 19: #Has between 1 and 20 words
                    line = line.replace(",", "")
                    line = line.replace(".", "")
                    line = line.replace(":", "")
                    result.append(line)"""
    

# Main Functions

def get_result_by_lang_directory(directory):
    result = list()
    pwd = os.getcwd() + "/" + directory
    print("At this moment, starting with " + pwd)
    for filename in os.listdir(pwd):
        print("Processing " + filename)
        lines = tuple(open(pwd + "/" + filename, 'r'))
        lines_processed = process_line(lines)
        result += lines_processed
    return result

def join_all_langs_into_list(lang_dict, lang_results):
    result = list()
    for key, value in lang_dict.items():
        for line in value:
            line = line.strip()
            if len(line.rstrip()) > 1:
                new_line = line.rstrip() + "-" + lang_results[key]
                result.append(new_line)
    return result

def save_files(train_file, eval_file):
    trainf = open('train.txt', 'w+')
    for item in train_file:
        trainf.write("%s\n" % item)
    print("train.txt saved!")
    trainf.close()
    evalf = open('eval.txt', 'w+')
    for item in eval_file:
        evalf.write("%s\n" % item)
    print("eval.txt saved!")
    evalf.close() 


# Main code

print("Init process...")

for directory in lang_directories:
    lang_result = get_result_by_lang_directory(directory)
    lang_dict[directory] = lang_result

print("All files processed...")

all_lang_result = join_all_langs_into_list(lang_dict, lang_results)

shuffle(all_lang_result)

print("Shuffeling...")

train_file = all_lang_result[:int(len(all_lang_result)/2)]
eval_file = all_lang_result[int(len(all_lang_result)/2):]

save_files(train_file, eval_file)

print("End! train.txt and eval.txt have been putting into this directory.")

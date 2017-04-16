#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script find .txt files in ['da', 'de', 'el', 'en', 'es', 'fi', 'it', 'fr', 'nl', 'pt'] directories to process it 
inside /txt directory from http://www.statmt.org/europarl/v7/europarl.tgz and it creates a single file for trainning and evaluation both.

The result will have a shuffle of differents languages sentences between 1 and 20 words lenght like this:

----------------------------------
this is an example of sentences-0 0 0 1 0 0 0 0 0 0
esto es un ejemplo de frase-0 0 0 0 1 0 0 0 0 0
c'est un exemple de phrase-0 0 0 0 0 0 1 0 0 0
----------------------------------

And, the result will have a million differents words per language for trainning, and finally, will have 100.000 differents words per language
for evaluation.
"""

# Imports

import os
from random import shuffle
from sklearn.feature_extraction.text import CountVectorizer

# Structures

lang_directories = ['da', 'de', 'el', 'en', 'es', 'fi', 'fr', 'it', 'nl', 'pt']

lang_results = {'da':'1 0 0 0 0 0 0 0 0 0', 'de':'0 1 0 0 0 0 0 0 0 0', 'el':'0 0 1 0 0 0 0 0 0 0', 'en':'0 0 0 1 0 0 0 0 0 0', 
'es':'0 0 0 0 1 0 0 0 0 0', 'fi':'0 0 0 0 0 1 0 0 0 0', 'fr':'0 0 0 0 0 0 1 0 0 0', 'it':'0 0 0 0 0 0 0 1 0 0', 'nl':'0 0 0 0 0 0 0 0 1 0', 
'pt':'0 0 0 0 0 0 0 0 0 1'}

lang_num_words = dict() 

lang_dict = dict()

invalid_character = ['<']
replace_character = ['.',',','"','(',')','–','−','_','/','-',':',';','0','1','2','3','4','5','6','7','8','9',
'«','=','&','%','…','„','<','>','’','»','[',']','º','”','+','$','€']

count_corpus = {'da':set(), 'de':set(), 'el':set(), 'en':set(), 'es':set(), 'fi':set(), 'fr':set(), 'it':set(), 'nl':set(), 'pt':set()}

vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2), min_df=1)

n_gram = set()

d_n_gram = dict()

# Secondary functions

def filter(line):
    return not any(x in line for x in invalid_character)

def replace(line):
    new_line = line
    for c in replace_character:
        new_line = new_line.replace(c,'')
    return new_line

def process_line(lines):
    result = list()
    for line in lines:
        if line and len(line) > 0 and filter(line) and line.count(' ') <= 19:
            new_line = replace(line)
            result.append(new_line)              
    return result

def report_corpus(line, key):
    l = line.split(' ')
    s = count_corpus[key]
    if s:
        count_corpus[key].update(l)
    else:
        count_corpus[key] = set(l)

def build_n_gram(line):
    vectorizer.fit_transform([line.lower()])
    names = vectorizer.get_feature_names()
    n_gram.update(list(names))


# Main Functions

def get_result_by_lang_directory(directory):
    result = list()
    pwd = os.getcwd() + "/" + directory
    print("Processing " + directory + " directory.")
    for filename in os.listdir(pwd):
        lines = tuple(open(pwd + "/" + filename, 'r'))
        lines_processed = process_line(lines)
        result += lines_processed
    return result

def join_all_langs_into_list(lang_dict, lang_results):
    result = list()
    for key, value in lang_dict.items():
        for line in value:
            line = line.strip()
            if len(line) > 1:
                new_line = line.rstrip() + "-" + lang_results[key]
                build_n_gram(line)
                report_corpus(line, key)
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

def save_n_gram():
    dngramf = open('ngram.txt', 'w+')
    dngramf.write(str(d_n_gram))

# Main code

print("Init process...")

print("Processing all files into directories...")

for directory in lang_directories:
    lang_result = get_result_by_lang_directory(directory)
    lang_dict[directory] = lang_result

print("All files processed...")

print("Joining all languages...")

all_lang_result = join_all_langs_into_list(lang_dict, lang_results)

print("Joining success!")

print("Shuffeling...")

shuffle(all_lang_result)

print("Shuffelinig success!")

print("Reporting of corpus...")

for key, value in count_corpus.items():
    print("Lang: " + key + ", corpus: " + str(len(value)))

print("Building n_gram dict...")

pos = 0
for gram in n_gram:
    d_n_gram[pos] = gram
    pos += 1

print("Saving files...")

save_n_gram()

train_file = all_lang_result[:int(len(all_lang_result)/2)]
eval_file = all_lang_result[int(len(all_lang_result)/2):]

save_files(train_file, eval_file)

print("End! train.txt and eval.txt have been putting into this directory.")
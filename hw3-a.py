#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:45:32 2018

@author: manoharsaijasti
"""

#importing the modules
import pickle
import sys
import time
import unicodedata
import math
import re
from collections import Counter
import operator

timeperfbeg  = time.perf_counter()
timeprocbeg  = time.process_time()
print("start at elapsed time : ",timeperfbeg," cpu time : ",timeprocbeg)      




#data(object)(list of dicts) = unigrams+bigrams+word_frequency
#pickle data  to data.dab 
unigrams_freq={}
#generating the unigrams
def unigrams(words):
    
        
    for word in words:
        
        for c in word:
            if c in unigrams_freq:
                unigrams_freq[c]+=1
            else:
                unigrams_freq[c]=1
bigram_freq = {}

#generating the bigrams
def bigrams(words):
        
        bigrams_list=[]

        from nltk.util import bigrams
        for s in words:
            s="<"+s+">"
        
            wordList = list(bigrams(s))
        
        
            for i in wordList:
                i=list(i)  
                bi=""
                for j in i:
                    bi=bi+j
                bigrams_list.append(bi)
        
    
        for bigram in bigrams_list:
        
            if bigram in bigram_freq:
                bigram_freq[bigram]+=1
            else:
                bigram_freq[bigram]=1
                
word_freq = {}
#generating the word frequncies
def word_frequency(words):
    
    
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    
    
input = "ap88.txt"    
file = open(input,"r")    
pattern = "AP88....-...."
lines_lowercase = []
total_words_length=0
for line in file:
    line= re.sub(pattern,' ',line)
    for c in line:
        if (ord(c) >=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122):
            line = line.replace(c,c.lower())
        else:
            line = line.replace(c," ")
    words_line = [word for word in line.split()]
    total_words_length = total_words_length + len(words_line)
    unigrams(words_line)
    bigrams(words_line)
    word_frequency(words_line)

timeperfend  = time.perf_counter()
timeprocend  = time.process_time()  
print("finish reading at elapsed time : ",timeperfend," cpu time : ",timeprocend)

totalelapsedtime = timeperfend - timeperfbeg

totalcputime = timeprocend - timeprocbeg

print("total elapsed time : ", totalelapsedtime," cpu time : " , totalcputime)


print("Number of words: " ,total_words_length)
print("Number of types (distinct words): ", len(word_freq))




print("Unigram counts:")
alpha_unigrams = dict(sorted(unigrams_freq.items(), key=lambda x: x[0]))
    
for k, v in alpha_unigrams.items():
    print(k, v)
    
print("Bigram Counts : ")
alpha_bigrams = dict(sorted(bigram_freq.items(), key=lambda x: x[0]))
    
for k, v in alpha_bigrams.items():
    print(k, v)




merge_dicts_list = []
merge_dicts_list.append(alpha_unigrams)
merge_dicts_list.append(alpha_bigrams)
merge_dicts_list.append(word_freq)
merge_dicts_list.append(total_words_length)

class Data(object):
    def __init__(self,data):
        self.data = data
    def mydata(self,data):
        return self.data

data_object = Data(merge_dicts_list)

mydata = data_object.mydata(merge_dicts_list)


        

with open("data1.dat", "wb") as f:
    pickle.dump(mydata, f)

#pickling the data
print("pickling done imported to ",f)





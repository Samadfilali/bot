#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from frames.utils import get_users_for_fold, key_value_pairs
import json
import re
import hashlib


# In[2]:


# to load jason frame
with open("C:/Users/samad/P10test/frames/data/frames.json") as json_data:
    data_dict = json.load(json_data)


# In[3]:


#generate train and test data
with open("frames.json") as f:
    dialogues = json.load(f)

fold = 1
test_users = get_users_for_fold(fold)
train_users = get_users_for_fold(-fold)

train_dialogues = [d for d in dialogues if d['user_id'] in train_users]
test_dialogues = [d for d in dialogues if d['user_id'] in test_users]


# In[4]:


# Liste des entités


# In[5]:


list_entities=['dst_city','or_city','budget','str_date','end_date']
file_path='fichier.temp'


# In[6]:


def extraction_of_information(dialogues,file_path, entities) :
    with open(file_path, 'w') as f:
        for  dialogue in dialogues :
            for turn in dialogue['turns'] :
                if turn['author'] =='user' :
                    for act in turn['labels']['acts'] :
                        if act['name']=='inform' :
                            texte=re.sub(r"[\n]*", "", turn['text'])
                            texte="- "+texte+" \n"
                            val_key = key_value_pairs(act)
                            for v in val_key : 
                                if v[0] in entities :
                                    texte=texte.replace(str(v[1]),"{@"+v[0]+"="+str(v[1])+"} ")
                f.writelines(texte)
                            


# In[7]:


def remove_duplicated_lines(input_file_path) :
    output_file_path = "FlightBooking.lu"
    #2
    completed_lines_hash = set()
    #3
    output_file = open(output_file_path, "w")
    output_file.write("# BookFlight \n\n")
    #4
    for line in open(input_file_path, "r"):
        #5
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        #6
        if hashValue not in completed_lines_hash:
            if "@" in line :
                line=line.replace("@or_city","@From")
                line=line.replace("@dst_city","@To")
                output_file.write(line)
                completed_lines_hash.add(hashValue)
    #7
    output_file.write(" \n\n")
    output_file.write("> # Composite entities \n\n")
    output_file.write("@ composite str_date = [datetimeV2] \n")
    output_file.write("@ composite end_date = [datetimeV2] \n")
    output_file.close()
    


# In[8]:


extraction_of_information(train_dialogues,file_path,list_entities)


# In[9]:


remove_duplicated_lines(file_path)


# In[ ]:





# -*- coding: utf-8 -*-
import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from difflib import SequenceMatcher
import json

start_time = time.time()

def similar(a, b):
    for x in a["Competence"]:
        for y in b["Competence"]:
            if SequenceMatcher(None, x, y).ratio()*100 > 80:
                return b["URL"]

def fuzz_similarity(a, b):
    for x in a["Competence"]:
        for y in b["Competence"]:
            if fuzz.ratio(x,y)>80:#similar(x, y) > 0.7:
                return b["URL"]

data = json.load(open('data.json'))
standarts = json.load(open('Ed_Standarts_ITMO_data.json'))
match_array = []

for i in range(len(standarts)):
    match_dict = {}
    match_dict["id"] = i
    match_dict["Directions"] = standarts[i]["Directions"]
    match_dict["Course_direction_match"] = []
    match_dict["Course_competence_match"] = []
    standart_to_courses = []
    for j in range(len(data)):
        for x in data[j]["Directions"]:
            if standarts[i]["Directions"][:3] == x[:3]:
                match_dict["Course_direction_match"].append(data[j]["URL"])
                break
        similar = fuzz_similarity(standarts[i],data[j])
        if similar:
            match_dict["Course_competence_match"].append(similar)
        #similar = similar(standarts[i],data[j])
        #if similar:
        #    match_dict["Course_competence_match"].append(similar)    
        
    match_dict["Course_competence_match"]=list(set(match_dict["Course_competence_match"]))        
    match_array.append(match_dict)


with open('results.json', 'w') as fp:
    json.dump(match_array, fp)                

        
print("Script ok! in %s seconds" % (time.time() - start_time))
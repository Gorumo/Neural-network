from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json

data = json.load(open('data.json'))
standarts = json.load(open('Ed_Standarts_ITMO_data.json'))

for i in range(len(standarts)):
    for j in range(len(standarts[i]["Competence"])):
        for k in range(len(data)):
        # if standarts[i]["Competence"][j] in data[k]["Competence"]:
        #print(fuzz.token_sort_ratio(b, a))
            if data[k]["Competence"]:
                for n in range(len(data[k]["Competence"])):
                    #max_similarity = max(data[k]["Competence"], key=lambda a: fuzz.ratio(a, standarts[i]["Competence"][j]))
                    
                    similarity = fuzz.partial_ratio(standarts[i]["Competence"][j], data[k]["Competence"][n])
                    if similarity >60:
                        print(standarts[i]["Competence"][j], ' - ',similarity, ' from ',data[k]["Title"])
#print(fuzz.ratio(b, a))

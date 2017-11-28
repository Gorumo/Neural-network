import json
from difflib import SequenceMatcher
from itertools import groupby

data = json.load(open('data.json'))
standarts = json.load(open('Ed_Standarts_ITMO_data.json'))

match_dict={}
course_array=[]
match_array=[]

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result

for os_direct in range(len(standarts)):
	#print (os_direct["Directions"])
	match_dict.clear()
	course_array=[]
	for course_direct_arrays in range(len(data)):
		for course_direct in range(len(data[course_direct_arrays]["Directions"])):
			if similar(data[course_direct_arrays]["Directions"][course_direct][:3], standarts[os_direct]["Directions"][:3]) > 0.99:
				#print (data[course_direct_arrays]["URL"] + "----" + standarts[os_direct]["Directions"])
				course_array.append(data[course_direct_arrays]["URL"])
	course_array_new = unique(course_array)
		#course_array_new = [el for el, _ in groupby(course_array)]
	#print (course_array_new)
	match_dict["Directions"] = standarts[os_direct]["Directions"]
	match_dict["Course_direction_match"]=course_array_new
	match_array.append(match_dict)

print(match_array)

#print (json.dumps(match_array))





#for i in range(len(standarts)):
    #for j in range(len(standarts[i]["Competence"])):
        #for k in range(len(data)):
        # if standarts[i]["Competence"][j] in data[k]["Competence"]:
        #print(fuzz.token_sort_ratio(b, a))
            

        	#for courses
            #for direct in range(len(data[k]["Directions"])):
            	#print(data[k]["Title"] + '  ------  ' + data[k]["Directions"][direct])
            	
            
                #for n in range(len(data[k]["Competence"])):
                    #similarity = fuzz.partial_ratio(standarts[i]["Competence"][j], data[k]["Competence"][n])
                    #if similarity >60:
                        #print(standarts[i]["Competence"][j], ' - ',similarity, ' from ',data[k]["Title"])

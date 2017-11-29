import json
from difflib import SequenceMatcher
from itertools import groupby

data = json.load(open('data.json'))
standarts = json.load(open('Ed_Standarts_ITMO_data.json'))

match_dict={}
course_array=[]
match_array=[]

#function for matching os direction and course direction indexes
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()
#function to delete dublicates from array
def unique(lst):
	seen = set()
	result = []
	for x in lst:
		if x in seen:
			continue
		seen.add(x)
		result.append(x)
	return result
k=0
#parsings of jsons and matching OS and courses by Direction
for os_direct in range(len(standarts)):
	match_dict={}
	course_array_new=[]
	course_array=[]
	for course_direct_arrays in range(len(data)):
		for course_direct in range(len(data[course_direct_arrays]["Directions"])):
			if similar(data[course_direct_arrays]["Directions"][course_direct][:3], standarts[os_direct]["Directions"][:3]) > 0.99:
				course_array.append(data[course_direct_arrays]["URL"])
	
	k=k+1
	match_dict["id"]=k
	match_dict["Directions"] = standarts[os_direct]["Directions"]
	course_array_new = unique(course_array)
	match_dict["Course_direction_match"]=course_array_new
	match_array.append(match_dict)
	

#After all we have an array of OS directions and fitable courses
for m in range(len(match_array)):
	print(match_array[m]["id"])
	print(match_array[m]["Directions"])
	print(match_array[m]["Course_direction_match"])
	

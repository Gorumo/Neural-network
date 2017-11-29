# -*- coding: utf-8 -*-
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
ma=0
#parsings of jsons and matching OS and courses by Direction
for os_direct in range(len(standarts)):
	match_dict={}
	course_array_new=[]
	course_array=[]
	course_array_comp=[]
	course_array_comp_new=[]
	#print(standarts[os_direct]["Directions"])
	#print(standarts[os_direct]["Competence"][0])
	#print("***********NEW__OS****************")	
	#Competence of OS
	for m in range(len(standarts[os_direct]["Competence"])):
		#print("___________OS Competence_________________")
		#print(standarts[os_direct]["Competence"][m])
		#Competens of course
		for course_direct_arrays in range(len(data)):
		#Competences matching
			for course_comp_arrays in range(len(data[course_direct_arrays]["Competence"])):
				if similar(data[course_direct_arrays]["Competence"][course_comp_arrays], standarts[os_direct]["Competence"][m])>0.9:
					#print("There's a match")
					course_array_comp.append(data[course_direct_arrays]["URL"])
					ma=ma+1
					#print("Course Competence", data[course_direct_arrays]["Competence"][course_comp_arrays])
					#print("OS Competence", standarts[os_direct]["Competence"][m])
					#print(ma)
				#print("Course Competence")
				#print(data[course_direct_arrays]["Competence"][course_comp_arrays])
			

		#Directions matching
	for course_direct_arrays in range(len(data)):
		for course_direct in range(len(data[course_direct_arrays]["Directions"])):
			if similar(data[course_direct_arrays]["Directions"][course_direct][:3], standarts[os_direct]["Directions"][:3]) > 0.99:
				course_array.append(data[course_direct_arrays]["URL"])
	#Directions list
	k=k+1
	match_dict["id"]=k
	match_dict["Directions"] = standarts[os_direct]["Directions"]
	course_array_new = unique(course_array)
	course_array_comp_new = unique(course_array_comp)
	match_dict["Course_direction_match"]=course_array_new
	match_dict["Course_competence_match"]=course_array_comp_new
	#Competence list

	match_array.append(match_dict)
	
#Match array is ready to make json dump
print(match_array)
#print(ma)
#After all we have an array of OS directions and fitable courses
#for o in range(len(match_array)):
	#print(match_array[o]["id"])
	#print(match_array[o]["Directions"])
	#print("Course_direction_match")
	#print(match_array[o]["Course_direction_match"])
	#print("Course_competence_match")
	#print(match_array[o]["Course_competence_match"])

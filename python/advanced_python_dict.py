import csv

f = open('faculty.csv') 
next(f) #skip first line
faculty_dict1 = {}
faculty_dict2 = {}
for line in f:
    entry = line.split(',')
    lastname = entry[0].split(' ')[-1]
    firstname = entry[0].split(' ')[0]
    degree = entry[1]
    title = entry[2].split('Professor')[0] + 'Professor'
    email = entry[-1].rstrip()
    
    #first dictionary (using last name as key)
    if faculty_dict1.has_key(lastname):
        faculty_dict1[lastname].append([degree, title, email])
    else:
        faculty_dict1[lastname] = [[degree, title, email]] 
        
    #second dictionary (using first and last name as key)
    faculty_dict2[(firstname,lastname)] = [degree, title, email]

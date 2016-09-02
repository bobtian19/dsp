import csv
f = open('faculty.csv') 
next(f) #skip first line
with open('output.csv', "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')    
    for line in f:
        email = line.split(',')[-1].rstrip() #get e-mail from line in faculty.csv
        writer.writerow([email]) #write it to output.csv

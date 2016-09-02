## Q1. Find how many different degrees there are, and their frequencies: 
## Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
f = open('faculty.csv') 
next(f) #skip first line
degrees = []
for line in f:
    temp = line.split(',')[1].strip().replace(".", "")
    if temp != '0':
        degrees += temp.split(' ')
#print the counts
print('There are ' + str(len(set(degrees))) + ' unique degrees')
for d in list(set(set(degrees))):
    print(d + ': ' + str(degrees.count(d)))
print #line skip
f.close()

## Q2. Find how many different titles there are, and their frequencies: 
## Ex: Assistant Professor, Professor
f = open('faculty.csv') 
next(f) #skip first line
titles = []
for line in f:
    fulltitle = line.split(',')[2]
    titles.append(fulltitle.split('Professor')[0] + 'Professor')
#print the counts
print('There are ' + str(len(set(titles))) + ' unique titles')
for t in list(set(set(titles))):
    print(t + ': ' + str(titles.count(t)))
print #lineskip
f.close()

## Q3. Search for email addresses and put them in a list. 
## Print the list of email addresses.
f = open('faculty.csv') 
next(f) #skip first line
emails = []
for line in f:
    emails.append(line.split(',')[-1].rstrip())
for e in emails:
    print e
print #lineskip
f.close()

## Q4. Find how many different email domains there are 
## (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). 
## Print the list of unique email domains.
domains = []
count = 0
for e in emails:
    domains.append(e.split('@')[-1])
for d in list(set(domains)):
    count += 1
    print d
print('There are ' + str(count) + ' unique e-mail domains.')

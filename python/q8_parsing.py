# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

f = open('football.csv') 
next(f) #skip first line
l_team = []
l_absgd = []
#populate list of team names and list of corresponding absolute goal difference
for line in f:
    temp = line.split(',')
    l_team.append(temp[0])
    l_absgd.append(abs(int(temp[5]) - int(temp[6])))

i = l_absgd.index(min(l_absgd))
print(l_team[i] + ' has the smallest absolute goal difference')

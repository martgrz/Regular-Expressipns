'''
Clean up dates in different date formats.
The standard format is dd.mm.yyyy
'''


import re

#read dates from tht file

file = open('dates.txt')
file = file.read()


#select dates in standard format
dmyRegex = re.compile(r'\d\d.\d\d.\d\d\d\d')
dmy = dmyRegex.findall(file)



#select dates in non-standard format
ymdRegex = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)')
ymd = ymdRegex.findall(file)


#convert dates to standard format
datesCleaned = []

for groups in ymd:
    newDate = '.'.join([groups[2],groups[1],groups[0]])
    datesCleaned.append(newDate)

#concatenate dates in one list
dates = dmy + datesCleaned

print(dates)
    

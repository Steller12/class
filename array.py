currentDay = int(input('What day of the month is it?'))
currentMonth = int(input('What month is it?'))
currentYear = int(input('What year is it?'))
birthDay = int(input('What day of the month were you born on?'))
birthMonth = int(input('What month were you born?'))
birthYear = int(input('Which year were you born in?'))
ageDays = currentDay - birthDay
ageMonths = currentMonth - birthMonth
ageYears = currentYear - birthYear
daysToAdd = 0

if currentMonth == 1 or currentMonth == 3 or currentMonth == 5 or currentMonth == 7:
    daysToAdd = 31

elif currentMonth == 2:
    daysToAdd = 28

elif currentMonth == 8 or currentMonth == 10 or currentMonth == 12:
    daysToAdd = 31

else:
    daysToAdd = 30

if birthDay > currentDay:
    ageMonths = ageMonths + 1
    ageDays = ageDays + daysToAdd

if birthMonth > currentMonth:
    ageMonths = ageMonths + 12

if birthYear < 2016:
    ageDays = ageDays + 1
    if birthYear < 2012:
        ageDays = ageDays + 1
        if birthYear < 2008:
            ageDays = ageDays + 1
            if birthYear < 2004:
                ageDays = ageDays + 1
                if birthYear < 2000:
                    ageDays = ageDays + 1
                    if birthYear < 1996:
                        ageDays = ageDays + 1

print('You are: ', ageYears, ' years, ', ageMonths, ' months, ', ageDays, ' days.')
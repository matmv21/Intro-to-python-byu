
gradePercentage = int(input('What is your grade percentage? '))

# GRADE ANALYSIS
if gradePercentage >= 90:
    gradeLetter = 'A'
elif gradePercentage >= 80:
    gradeLetter = 'B'
elif gradePercentage >= 70:
    gradeLetter = 'C'
elif gradePercentage >= 60:
    gradeLetter = 'D'
else:
    gradeLetter = 'F'

# ADDITIONAL ANALYSIS
last_digit = int(str(gradePercentage)[-1])
if last_digit >= 7 and gradeLetter != 'A' and gradeLetter != 'F':
    gradeLetter = gradeLetter + '+'
elif last_digit < 3 and gradeLetter != 'F':
    gradeLetter = gradeLetter + '-'

# PRINTING THE RESULTS
if gradePercentage >= 70:
    print(gradeLetter)
    print('Congratulations! You passed.')
else:
    print(gradeLetter)
    print('Sorry! Keep up for next time.')
# Practcing "if-elif-else"


score = float(input('Enter your score: '))

if score >= 90:
    print('Your grade is A.')
elif score >= 80:
    print('Your grade is B.')
elif score >= 70:
    print('Your grade is C.')
elif score >= 60:
    print('Your grade is D.')
else:
    print('Your grade is F.')
    
# Practcing "And Or Not"


if 10 < 20 and 24 > 12: # Two condtion must be true
    print('And condtion is working!\n')
    
if 10 < 20 or 24 < 12: # One condtion must be true
    print('Or test condtion is working!\n')
    
if not (5>10): # not true is false and vice versa!
    print('Not testing condtion is working!\n')


# Practcing Boolean exprsion

hungry = True
sleepy = False

if hungry:
    print('Yea, I\'m Hungry') 
else:
    print('I\'m not, Hungry')
if sleepy:
    print('True')
else:
    print('I\'m not a sleep because I\'m telling you!')

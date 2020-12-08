# Task 1
import string
text = input()
text = text.upper()
count = 0
max = 0
letter = ''
for i in string.ascii_uppercase:
    count = text.count(i)
    if count > max:
        max = count
        letter = i
print(max, '-', letter)
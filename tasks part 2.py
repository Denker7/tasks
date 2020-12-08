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

# Task 2
text = input()
count = 0
for i in text.split():
    if i.isalpha():
        count += 1
    else:
        count = 0
    if count == 3:
        print("есть последовательность из 3 слов")
        break;
if count < 3:
    print ('отсутствует последовательность из 3 слов')

# Task 3
text = input()
count = 1
max = 1
for i in range(1,len(text)):
    if text[i] == text[i-1]:
        count += 1
        if count > max:
            max = count
    else:
        count = 1
print(max)

# Task 4
text = input()
string = ''
for i in range(0,len(text)):
    if text[i].isupper():
        string += text[i]
print(string)

# Task 5
mass = input()
output = []
count = 0
for i,j in enumerate(mass):
    if i == mass.index(j):
        for count in range(mass.count(j)):
            output.extend([j])
print (output)

# Task 6
list1 = input()
number = int(input())
nearest = 0
min = number
for i in list1:
    if min > abs(number-int(i)):
        min = abs(number-int(i))
        nearest = i
    if min == abs(number-int(i)):
        if nearest > i:
            nearest = i
print('ближайшее к', number, 'является', nearest)
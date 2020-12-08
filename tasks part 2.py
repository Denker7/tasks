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
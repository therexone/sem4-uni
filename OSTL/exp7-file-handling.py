# program to illustrate file handling in python

import os 
files = os.listdir(os.curdir)
print(f'Files in current directory:\n{files}\n')

# create a file and write to it
file = open('file.txt', 'a+')
file.write(input('Write some content to the file:\n') + '\n')
file.seek(0)
print(f'Content in file:\n {file.read()}')


# appending data to the file
print('Appending data to the file....')
for i in range(5):
    file.write(f'This is line {i+2}\n')
file.seek(0)
print(f'Content in file:\n {file.read()}')


# count number of lines, words and characters
line_count = 0
word_count = 0
char_count = 0
file.seek(0)
for line in file:
    line_count += 1
    words = line.strip().split()
    word_count += len(words)
    for word in words:
        char_count += len(word)
        
print(f'Number of lines in the file: {line_count}')
print(f'Number of words in the file: {word_count}')
print(f'Number of characters in the file: {char_count}')

file.close()


""" -----OUTPUT----
student@student-X556UQK:~/Desktop/workspace/sem4-uni/OSTL$ python3 exp7-file-handling.py 
Files in current directory:
['exp4-tuples.py', 'exp1-swapping.py', 'exp7-file-handling.py', 'exp2-functions.py', 'exp6-dictionaries.py', 'exp3-lists.py']

Write some content to the file:
This is some text       
Content in file:
 This is some text

Appeding data to the file....
Content in file:
 This is some text
This is line 2
This is line 3
This is line 4
This is line 5
This is line 6

Number of lines in the file: 6
Number of words in the file: 24
Number of characters in the file: 69
student@student-X556UQK:~/Desktop/workspace/sem4-uni/OSTL$ 
"""
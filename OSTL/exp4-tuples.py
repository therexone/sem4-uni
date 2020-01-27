# program to demonstrate tuple usage
from functools import cmp_to_key

def create_tuple():
    roll_no = int(input('Enter Roll Number: '))
    name = input('Enter Student Name: ')
    mark1 = int(input('Enter mark for subject one: '))
    mark2 = int(input('Enter mark for subject two: '))
    mark3 = int(input('Enter mark for subject three: '))
    marks = (mark1, mark2, mark3)
    return (roll_no, name, marks)

def compare_name(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return -1

student_list = []
choice = ''

while choice != 5:
    print('--------TUPLE DEMO--------')
    print('1. Enter Student details\n2.Show Student Details\n3.Search for Python\n4.Sort\n5.Exit\n')
    choice = int(input('Enter option (1-5): '))
    if choice == 1:
        student_list.append(create_tuple())
    elif choice == 2:
        for student in student_list:
            print(student)
        print()
    elif choice == 3:
        for student in student_list:
            flag = 0
            if student[1] == "Python":
                print('Found Student \'Python\'')
                print(student)
                flag = 1
                break
        if flag == 0:
            print('\'Python\' not Found!\n')

    elif choice == 4:
        sorted_list = sorted(student_list, key=cmp_to_key(compare_name))
        print('Sorted List: ', sorted_list)


 """ -----------OUTPUT----------
 therexone@therexone-X556UQK:~/Desktop/workspace/sem4-uni/OSTL$ python3 exp4-tuples.py 
--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 1
Enter Roll Number: 98
Enter Student Name: Json 
Enter mark for subject one: 88
Enter mark for subject two: 45
Enter mark for subject three: 67
--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 1
Enter Roll Number: 89
Enter Student Name: Ayus
Enter mark for subject one: 983
Enter mark for subject two: 99
Enter mark for subject three: 84
--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 1
Enter Roll Number: 90
Enter Student Name: Zeus
Enter mark for subject one: 93
Enter mark for subject two: 97
Enter mark for subject three: 99
--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 2
(98, 'Json', (88, 45, 67))
(89, 'Ayus', (983, 99, 84))
(90, 'Zeus', (93, 97, 99))

--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 3
'Python' not Found!

--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 4
Sorted List:  [(89, 'Ayus', (983, 99, 84)), (98, 'Json', (88, 45, 67)), (90, 'Zeus', (93, 97, 99))]
--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 1
Enter Roll Number: 97
Enter Student Name: Python
Enter mark for subject one: 99
Enter mark for subject two: 99
Enter mark for subject three: 99
--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 3
Found Student 'Python'
(97, 'Python', (99, 99, 99))

--------TUPLE DEMO--------
1. Enter Student details
2.Show Student Details
3.Search for Python
4.Sort
5.Exit

Enter option (1-5): 5

"""
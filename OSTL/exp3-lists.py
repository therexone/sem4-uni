# menu driven program to illustrate use of list

print("-----------List Demo Program----------")

even_list = []
odd_list = []
merged_list = []
raw_list = []
choice = ''


def parity(n):
    return True if n % 2 == 0 else False

def add_integer_to_list(val):
    even_list.append(int(val)) if (val.isdigit() and parity(int(val))) else (
        odd_list.append(int(val)) if (val.isdigit() and not parity(int(val))) else 'false')

def minimum_integer():
    return min(odd_list) if min(odd_list) < min(
            even_list) else min(even_list)
def maximum_integer():
    return max(odd_list) if max(odd_list) > max(
            even_list) else max(even_list)

def add_integer_at_index(index, element):
     even_list.insert(index, int(element)) if (element.isdigit() and parity(int(element))) else (
                odd_list.insert(index, int(element)) if (element.isdigit() and not parity(int(element))) else 'false')

while choice != 9:
    print("1. Enter an element\n2. View Lists\n3. Merge Lists\n4. Sort List")
    print("5. Minimum element\n6. Maximum element\n7. Update element\n8. Search for 'Python'\n9. Press 9 to exit")
    choice = int(input())
    print('-----------------------------------------')
    if choice == 1:
        val = input('Enter element to add to list: ')
        raw_list.append(val)
        print('Added to list: ', val)
        add_integer_to_list(val)

    elif choice == 2:
        print('Raw List', raw_list)
        print('Odd List', odd_list)
        print('Even List', even_list)
        print('Merged List', merged_list)
        print()
        
    elif choice == 3:
        merged_list = list(set(odd_list + even_list))
        print('Merged List: ', merged_list)

    elif choice == 4:
        merged_list.sort()
        print('Sorted List: ', merged_list)
        
    elif choice == 5:
        minum = minimum_integer()
        print('Minumum number is ', minum)
    elif choice == 6:
        maxum = maximum_integer()
        print('Maximum Number is: ', maxum)
    elif choice == 7:
        index = int(input('Enter index to update: '))
        if len(raw_list) > index:
            element = (input('Enter element to update: '))
            raw_list.append(element)
            add_integer_at_index(index, element)
        else:
            print('Index out of Range')
    elif choice == 8:
        print('Found Python!' if 'python' or 'Python' in raw_list else 'Could not find Python!')
           
#---------------OUTPUT--------------------

# student@ubuntu~/Desktop/workspace/sem4-uni/OSTL$ python3 lists.py 
# -----------List Demo Program----------
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: 1
# Added to list:  1
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: 2
# Added to list:  2
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: 3
# Added to list:  3
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: 4
# Added to list:  4
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: 5
# Added to list:  5
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: 6
# Added to list:  6
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 2
# -----------------------------------------
# Raw List ['1', '2', '3', '4', '5', '6']
# Odd List [1, 3, 5]
# Even List [2, 4, 6]
# Merged List []

# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 3
# -----------------------------------------
# Merged List:  [1, 2, 3, 4, 5, 6]
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 4
# -----------------------------------------
# Sorted List:  [1, 2, 3, 4, 5, 6]
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 5
# -----------------------------------------
# Minumum number is  1
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 6
# -----------------------------------------
# Maximum Number is:  6
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 7
# -----------------------------------------
# Enter index to update: 2
# Enter element to update: 18 
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 2
# -----------------------------------------
# Raw List ['1', '2', '3', '4', '5', '6', '18']
# Odd List [1, 3, 5]
# Even List [2, 4, 18, 6]
# Merged List [1, 2, 3, 4, 5, 6]

# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 3
# -----------------------------------------
# Merged List:  [1, 2, 3, 4, 5, 6, 18]
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: "John"
# Added to list:  "John"
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: "cena"
# Added to list:  "cena"
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 1
# -----------------------------------------
# Enter element to add to list: "Python"
# Added to list:  "Python"
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 8
# -----------------------------------------
# Found Python!
# 1. Enter an element
# 2. View Lists
# 3. Merge Lists
# 4. Sort List
# 5. Minimum element
# 6. Maximum element
# 7. Update element
# 8. Search for 'Python'
# 9. Press 9 to exit
# 9
# -----------------------------------------
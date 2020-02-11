# program to illustrate usage of dictionary
dictionary = {}

while True:
    print('------Python Dictionary Demo-----')
    print('\n1.Create and add a key:value pair\n2.Update/Concatenate item\n3.Find a Key\n4.Map lists to dictionary\n5.Show Dictionary\n')
    choice = int(input('Select an option to coninue, press 0 to exit: '))

    if choice == 1 or choice == 2:
        dictionary[input('Enter Key: ')] = input('Enter Value: ')
        print(f'\nUpdated Dictionary\n{dictionary}\n')
    elif choice == 3:
        key_to_find = input('Enter the key to find: ')
        if key_to_find in dictionary:
            print(f'\nFound key: {key_to_find}, its value is {dictionary[key_to_find]}\n')
        else:
            print('\nKey Not Found!\n')
    elif choice == 4:
        list1 = [key for key in input('Enter keys: ').strip().split()]
        list2 = [key for key in input('Enter values: ').strip().split()]
        dictionary.update(dict(zip(list1, list2)))
        print(f'\nUpdated Dictionary\n{dictionary}\n')
    elif choice == 5:
        print(f'\n{dictionary}\n')
    else:
        break


"""------OUTPUT---------

student@student-X556UQK:~/Desktop/workspace/sem4-uni/OSTL$ python3 exp6-dictionaries.py 
------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 1
Enter Value: one
Enter Key: 1

Updated Dictionary
{'1': 'one'}

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 1
Enter Value: two
Enter Key: 2

Updated Dictionary
{'1': 'one', '2': 'two'}

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 1
Enter Value: python
Enter Key: 3

Updated Dictionary
{'1': 'one', '2': 'two', '3': 'python'}

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 2
Enter Value: lambda
Enter Key: 2

Updated Dictionary
{'1': 'one', '2': 'lambda', '3': 'python'}

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 3
Enter the key to find: 3

Found key: 3, its value is python

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 4
Enter keys: 9 7 5
Enter values: jason yer mum

Updated Dictionary
{'1': 'one', '2': 'lambda', '3': 'python', '9': 'jason', '7': 'yer', '5': 'mum'}

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 5

{'1': 'one', '2': 'lambda', '3': 'python', '9': 'jason', '7': 'yer', '5': 'mum'}

------Python Dictionary Demo-----

1.Create and add a key:value pair
2.Update/Concatenate item
3.Find a Key
4.Map lists to dictionary
5.Show Dictionary

Select an option to coninue, press 0 to exit: 0 
"""
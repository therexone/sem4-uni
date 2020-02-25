#python program to perform operations on lists, sets, tuple

#list
some_list = [ i for i in input('Enter List items: ').strip().split()]
print(f"The List is : {some_list}")
print("Elements in the list are:")
for element in some_list: 
    print(element)
print(f"The length of the list is: {len(some_list)}")

#set
some_set = { i for i in input('\nEnter set elements: ').strip().split()}
print(f"The set is : {some_set}")
print("Elements in the set are:")
for element in some_set: 
    print(element)
print(f"The length of the set is: {len(some_set)}")

#tuple
some_tuple = tuple([i for i in input('\nEnter tuple items: ').strip().split()])
print(f"The tuple is : {some_tuple}")
print("Elements in the list are:")
for element in some_tuple: 
    print(element)
print(f"The length of the tuple is: {len(some_tuple)}")


"""-----OUTPUT------

therexone@therexone-X556UQK:~/Desktop/workspace/sem4-uni/OSTL$ python3 assignment-
1-q1.py 
Enter List items: bananas apples milk 
The List is : ['bananas', 'apples', 'milk']
Elements in the list are:
bananas
apples
milk
The length of the list is: 3

Enter set elements: 2012 2016 2020 2024
The set is : {'2016', '2020', '2012', '2024'}
Elements in the set are:
2016
2020
2012
2024
The length of the set is: 4

Enter tuple items: 8 key 0 weather 
The tuple is : ('8', 'key', '0', 'weather')
Elements in the list are:
8
key
0
weather
The length of the tuple is: 4
"""
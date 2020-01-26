# program to swap two numbers and check the sign of the first number

number_a = int(input('Enter first Number a: '))

number_b = int(input('Enter second Number b: '))

print("Numbers entered, a = {}, b = {}".format(number_a, number_b))

# swap
number_a, number_b = number_b, number_a

print("Numbers after swap, a = {}, b = {}".format(number_a, number_b))
print('a is negative' if number_a < 0 else ('a is 0' if number_a ==0 else 'a is positive') )



#----------OUTPUT--------------

# student@ubuntu~/Desktop/workspace/sem4-uni/OSTL$ python3 exp1-swapping.py 
# Enter first Number a: 2
# Enter second Number b: 3
# Numbers entered, a = 2, b = 3
# Numbers after swap, a =3, b = 2
# a is positive
# student@ubuntu~/Desktop/workspace/sem4-uni/OSTL$ python3 exp1-swapping.py 
# Enter first Number a: -1
# Enter second Number b: -2
# Numbers entered, a = -1, b = -2
# Numbers after swap, a = -2, b = -1
# a is negative
# student@ubuntu~/Desktop/workspace/sem4-uni/OSTL$ python3 exp1-swapping.py 
# Enter first Number a: 0
# Enter second Number b: 0
# Numbers entered, a = 0, b = 0
# Numbers after swap, a = 0, b = 0
# a is 0

# menu driven program to check if string is palindrome and find the factorial of the input number

def factorial(n):     
    if n == 1 or n == 0  :
        return 1
    elif n < 0:
        print('Error! Cannot find factorial for a negative number\nQuitting.....')
        exit(0)
    else: 
        return n*factorial(n-1)

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


while True:
    print('------PALINDROME CHECKER AND FACTORIAL FINDER-------')
    print('1. Calculate factorial\n2.Check string for palindrome\n3.Quit')

    choice = int(input('Select an option to continue: '))

    if choice == 1:
        number = int(input('Enter a number to calculate factorial of: '))
        print('The factorial of {} is {}\n'.format(number, factorial(number)))
    elif choice == 2:
        string = input('Enter the word: ')
        print('The string \'{}\' is a Palindrome\n'.format(string) if palindrome(string) else 'The string \'{}\' is not a palindrome\n'.format(string))
    elif choice == 3:
        exit(0)

#--------------OUTPUT-----------------

# student@ubuntu~/Desktop/workspace/sem4-uni/OSTL$ python3 exp2-functions.py
# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 1
# Enter a number to calculate factorial of: 6
# The factorial of 6 is 720

# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 1   
# Enter a number to calculate factorial of: 0
# The factorial of 0 is 1

# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 1
# Enter a number to calculate factorial of: -3
# Error! Cannot find factorial for a negative number
# Quitting.....
# student@ubuntu~/Desktop/workspace/sem4-uni/OSTL$ python3 exp2-functions.py
# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 2
# Enter the word: xanax
# The string 'xanax' is a Palindrome

# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 2
# Enter the word: sifhiesa
# The string 'sifhiesa' is not a palindrome

# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 2
# Enter the word: 
# The string '' is a Palindrome

# ------PALINDROME CHECKER AND FACTORIAL FINDER-------
# 1. Calculate factorial
# 2.Check string for palindrome
# 3.Quit
# Select an option to continue: 3
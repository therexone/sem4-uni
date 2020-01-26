# menu driven program to illustrate use of list

print("-----------List Demo Program----------")

even_list = []
odd_list = []
merged_list = []
raw_list = []
choice = ''


def parity(n):
    return True if n % 2 == 0 else False


while choice != 8:
    print("1.Enter an element\n2. View Lists\n3.Merge Lists\n4.Sort List")
    print("5.Minimum element\n6.Maximum element\n7.Update element\n8.Press 8 to exit")
    choice = int(input())
    print('-----------------------------------------')
    if choice == 1:
        val = input('Enter element to add to list: ')
        raw_list.append(val)
        print('Added to list: ', val)
        even_list.append(val) if (val.isdigit() and parity(int(val))) else (
            odd_list.append(val) if (val.isdigit() and not parity(int(val))) else 'false')
    elif choice == 2:
        print('Raw List', raw_list)
        print('Odd List', odd_list)
        print('Even List', even_list)
        print('Merged List', merged_list)
        print()
    elif choice == 3:
        merged_list.extend(odd_list)
        merged_list.extend(even_list)
        print(merged_list)
    elif choice == 4:
        print(merged_list.sort())
    elif choice == 5:
        minum = min(odd_list) if min(odd_list) < min(
            even_list) else min(even_list)
        print('Minumum number is ', minum)
    elif choice == 6:
        maxum = max(odd_list) if max(odd_list) > max(
            even_list) else max(even_list)
        print('Maximum Number is: ', maxum)
    elif choice == 7:
        index = int(input('Enter index to update: '))
        if len(raw_list) > index:
            element = (input('Enter element to update: '))
            raw_list.append(element)
            even_list.insert(index, element) if (element.isdigit() and parity(int(element))) else (
                odd_list.insert(index, element) if (element.isdigit() and not parity(int(element))) else 'false')

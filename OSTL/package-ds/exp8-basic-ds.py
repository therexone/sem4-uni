# program to implement stack, queue and linked list in python using packages

from queue import queue
from stack import stack
from lists import lists as linked_list

while True:
    print('-------BASIC DATA STRUCTURE IMPLEMENTAION IN PYTHON-------\n1.Stack\n2.Queue\n3.Linked List')
    choice = int(
        input('Enter options(1-3) or press any other number key to exit: '))

    if choice == 1:
        size = int(input('Enter stack size: '))
        stack = stack(size)
        print(f'Stack created with size: {size}')
        while True:
            print('\n-----STACK-----\n1.Push\n2.Pop\n3.Display Stack')
            sub_choice = int(
                input('Enter options(1-3) or press any other number key to go back: '))
            if sub_choice == 1:
                stack.push(input('Enter element: '))
            elif sub_choice == 2:
                print(f'\nPopped element: {stack.pop()}\n')
            elif sub_choice == 3:
                print(stack.get_stack())
            else:
                break
    elif choice == 2:
        size = int(input('Enter queue size: '))
        queue = queue(size)
        print('\n-----QUEUE-----\n1.Add to queue\n2.Dequeue\n3.Display queue')
        while True:
            sub_choice = int(
                input('Enter options(1-3) or press any other number key to go back: '))
            if sub_choice == 1:
                queue.push_to_queue(input('Enter element: '))
            elif sub_choice == 2:
                print(f'\nDequeued element: {queue.dequeue()}\n')
            elif sub_choice == 3:
                print(queue.get_queue())
            else:
                break
    elif choice == 3:
        linked_list = linked_list()
        while True:
            print('\n--------LINKED LIST------\n1.Add element(end)\n2.Add Element(front)\n3.Delete(end)\n4.Delete(front)\n5.Insert at an index\n6.Delete at an index\n7.Display List')
            sub_choice = int(
                input('Enter a choice(1-6) or press any other number to exit: '))
            if sub_choice == 1:
                linked_list.add_to_end((input('Enter Element to add: ')))
            elif sub_choice == 2:
                linked_list.add_to_start(input('Enter element to add at front: '))
            elif sub_choice == 3:
                linked_list.delete_at_end()
            elif sub_choice == 4:
                linked_list.delete_at_start()
            elif sub_choice == 5:
                index = int(input('Enter index: '))
                element = input('Enter element: ')
                linked_list.insert_at_index(index, element)
            elif sub_choice == 6:
                index = int(input('Enter index: '))
                linked_list.delete_at_index(index)
            elif sub_choice == 7:
               linked_list.display_list()
            else:
                break

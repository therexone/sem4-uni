# program to implement stack, queue and linked list in python

from collections import deque

# stack - LIFO


class stack:
    def __init__(self, size):
        self.size = size
        self.list = []

    def push(self, element):
        if (len(self.list) != self.size):
            self.list.append(element)
        else:
            print('Stack Overflow.')

    def pop(self):
        try:
            return self.list.pop()
        except IndexError:
            print('\nStack is empty, try pushing some elements to the stack.')

    def get_stack(self):
        return self.list


# #queue - FIFO
class queue:
    def __init__(self, size):
        self.size = size
        self.queue = deque([], size)

    def push_to_queue(self, element):
        self.queue.append(element) if (len(self.queue) !=
                                       self.size) else print('Queue Overflow.')

    def dequeue(self):
        try:
            return self.queue.popleft()
        except IndexError:
            print('Queue is empty, try pushing some elements to the queue.')

    def get_queue(self):
        return self.queue


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
        linked_list = []
        while True:
            print('\n--------LINKED LIST------\n1.Add element(end)\n2.Add Element(front)\n3.Delete(end)\n4.Delete(front)\n5.Insert at an index\n6.Delete at an index\n7.Display List')
            sub_choice = int(
                input('Enter a choice(1-6) or press any other number to exit: '))
            
            if sub_choice == 1:
                linked_list.append(input('Enter Element to add: '))
            elif sub_choice == 2:
                linked_list.insert(0, input('Enter element to add at front: '))
            elif sub_choice == 3:
                print(f'Deleted from end: {linked_list.pop()}') if len(
                    linked_list) != 0 else print('No Element in stack try adding some\n')
            elif sub_choice == 4:
                print(f'Deleted from start: {linked_list.pop(0)}') if len(
                    linked_list) != 0 else print('No Element in stack try adding some\n')
            elif sub_choice == 5:
                linked_list.insert(int(input('Enter Index: ')),
                                   input('Enter element: '))
            elif sub_choice == 6:
                print(f'Deleted from index: {linked_list.pop(int(input("Enter Index: ")))}') if len(
                    linked_list) != 0 else print('No Element in stack try adding some\n')
            elif sub_choice == 7:
                print(linked_list)
            else:
                break
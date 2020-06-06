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


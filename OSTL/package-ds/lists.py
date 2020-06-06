#list

class lists:
    def __init__(self):
        self.linked_list = []
    def add_to_end(self, element):
        self.linked_list.append(element)
    def add_to_start(self, element):
        self.linked_list.insert(0, element)
    def insert_at_index(self, index, element):
        self.linked_list.insert(index, element)
    def delete_at_end(self):
        return self.linked_list.pop() if len(self.linked_list) != 0 else print('No element in linked list')
    def delete_at_start(self):
        return self.linked_list.pop(0) if len(self.linked_list) != 0 else print('No element in linked list')
    def delete_at_index(self, index):
        return self.linked_list.pop(index) if len(self.linked_list) != 0 else print('No element in linked list')
    def display_list(self):
        print(self.linked_list)
        
    
#  File: TestLinkedList.py

#  Description:

#  Student Name: Gabriel Mount

#  Student UT EID: GMM2767

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/03/2020

#  Date Last Modified:


import copy


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'Link(data={self.data}, next={self.next})'


class LinkedList(object):
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        n = 0
        current = self.first

        while current.next is not None:
            n += 1
            current = current.next

        return n

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if current is None:
            self.first = new_link
            return

        while current.next is not None:
            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        current = self.first
        if current is None:
            self.first = Link(data)
        else:
            while current.next is not None and data >= current.data:
                current = current.next
            if data < current.data:
                current.next = Link(current.data, current.next)
                current.data = data
            else:
                current.next = Link(data)

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        while current is not None and current.data != data:
            current = current.next
        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        while current is not None and current.data < data:
            current = current.next
        return current if current is None or current.data == data else None

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        current = self.first
        if current is None:
            return None

        while current.next is not None:
            if current.next.data == data:
                my_link = Link(current.next.data)
                current.next = current.next.next
                return my_link
            current = current.next

        return None

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        string = ''
        count = 0
        current = self.first
        while current is not None:
            string += f'{current.data} '
            count += 1
            current = current.next
            if count % 10 == 0:
                string += '\n'
        return string

    # Copy the contents of a list and return new list
    def copy_list(self):
        new = LinkedList()

        def link_it(current):
            if current is None:
                return None
            else:
                return Link(current.data, next=link_it(current.next))

        new.first = link_it(self.first)
        return new

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        current = self.first
        new_list = LinkedList()
        while current is not None:
            new_list.insert_first(current.data)
            current = current.next
        return new_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        new_list = LinkedList()
        current = self.first
        while current is not None:
            new_list.insert_in_order(current.data)
            current = current.next
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        if current is None:
            return True
        while current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first is None

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        new = self.copy_list()
        current = new.first
        if current is None:
            new.first = other.first
            return new.sort_list() if not new.is_sorted() else new

        while current.next is not None:
            current = current.next
        current.next = other.first

        return new.sort_list() if not new.is_sorted() else new

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current1 = self.first
        current2 = other.first
        while current1 is not None and current2 is not None and current1.data == current2.data:
            current1 = current1.next
            current2 = current2.next

        return current1 is None and current2 is None

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        new = self.copy_list()
        current = new.first
        if current is None:
            return new

        while current is not None and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            current = current.next

        return new


def main():
    n = int(input())
    my_list = LinkedList()

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    for i in range(n):
        my_list.insert_first(int(input()))
    print(my_list, end='\n\n')

    # Test method insert_last()
    my_list.insert_last(14)
    print(my_list, end='\n\n')

    # Test method insert_in_order()
    my_list.insert_in_order(5)
    print(my_list, end='\n\n')

    # Test method get_num_links()
    print(my_list.get_num_links(), end='\n\n')

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    my_list.insert_last(-1)
    print(my_list.find_unordered(-1))
    print(my_list.find_unordered(-2))
    print(LinkedList().find_unordered(-1), end='\n\n')

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print(my_list.find_ordered(13))
    print(LinkedList().find_ordered(-1))
    my_list.insert_in_order(13)
    print(my_list.find_ordered(13), end='\n\n')

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print(my_list.delete_link(11))
    print(my_list.delete_link(12))
    print(LinkedList().delete_link(-1), end='\n\n')

    # Test method copy_list()
    print(my_list.copy_list(), end='\n\n')

    # Test method reverse_list()
    print(my_list.reverse_list(), end='\n\n')

    # Test method sort_list()
    print(my_list.sort_list())
    print(my_list.reverse_list().sort_list(), end='\n\n')

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(my_list.is_sorted())
    print(my_list.sort_list().is_sorted(), end='\n\n')

    # Test method is_empty()
    print(my_list.is_empty())
    print(LinkedList().is_empty(), end='\n\n')

    # Test method merge_list()
    print(my_list.merge_list(my_list.reverse_list()))
    print(LinkedList().merge_list(my_list))
    print(my_list.merge_list(LinkedList()), end='\n\n')

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(my_list.is_equal(my_list.copy_list()))
    print(LinkedList().is_equal(LinkedList()))
    print(my_list.is_equal(my_list.reverse_list()), end='\n\n')

    # Test remove_duplicates()
    print(my_list.copy_list().merge_list(my_list).remove_duplicates())


if __name__ == "__main__":
    main()

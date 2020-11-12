import sys


class Link(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = Link()
        self.first.next = self.first

    # Insert an element (value) in the list
    def insert(self, data):
        current = self.first
        if current.data is None:
            current.data = data
        else:
            while current.next != self.first:
                current = current.next
            current.next = Link(data, self.first)

    # Find the link with the given data (value)
    def find(self, data):
        current = self.first
        while current.data != data:
            current = current.next
        return current

    # Delete a link with a given data (value)
    def delete(self, data):
        current = self.first
        while current.next.data != data:
            current = current.next
        if self.first == current.next:
            self.first = current.next.next
        current.next = current.next.next

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        current = self.first
        if start == 1:
            while current.next != self.first:
                current = current.next
        else:
            current = self.find(start - 1)

        while self.first.next != self.first:
            for i in range(n):
                current = current.next
            print(current.data)
            self.delete(current.data)

        current = current.next
        print(current.data)

    # Return a string representation of a Circular List
    def __str__(self):
        string = ''
        current = self.first
        while current.next != self.first:
            string += f'{current.data} '
            current = current.next
        string += f'{current.data}'
        return string


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)
    circle = CircularList()
    for i in range(1, num_soldiers + 1):
        circle.insert(i)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    circle.delete_after(start_count, elim_num)


if __name__ == "__main__":
    main()

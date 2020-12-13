#  File: Radix.py

#  Description:

#  Student Name: Gabriel Mount

#  Student UT EID: GMM2767

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/02/2020

#  Date Last Modified: 11/02/2020

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    if len(a) == 0:
        return []

    queues = [Queue() for i in range(36)]
    keys = {}
    for i in range(10):
        keys[str(i)] = i
    for ind, i in enumerate(range(ord('a'), ord('z')+1)):
        keys[chr(i)] = ind + 10
    max_l = len(max(a, key=lambda p: len(p)))

    for i in range(max_l, -1, -1):
        sorted_list = []
        for word in a:
            if i >= len(word):
                queues[0].enqueue(word)
            else:
                queues[keys[word[i]]].enqueue(word)
        for queue in queues:
            while not queue.is_empty():
                sorted_list.append(queue.dequeue())
        a = sorted_list[:]

    return a


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()

#  File: Reducible.py

#  Description:

#  Student Name: Gabriel Mount

#  Student UT EID: GMM2767

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/27/2020

#  Date Last Modified: 10/30/2020


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    key = hash_word(s, const)
    return const - (key % const)


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    n = len(hash_table)
    ind = hash_word(s, n)
    if hash_table[ind] == '':
        hash_table[ind] = s
    else:
        step = step_size(s, 13)
        i = 1
        while hash_table[(ind + step * i) % n] != '':
            i += 1
        hash_table[(ind + step * i) % n] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    n = len(hash_table)
    ind = hash_word(s, n)
    if hash_table[ind] == s:
        return True
    elif hash_table[ind] != '':
        step = step_size(s, 13)
        i = 1
        while hash_table[(ind + step * i) % n] != '':
            if hash_table[(ind + step * i) % n] == s:
                return True
            i += 1
    return False


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    ns = len(s)
    if ns == 1:
        return s == 'a' or s == 'i' or s == 'o'
    elif find_word(s, hash_memo):
        return True
    else:
        for i in range(ns):
            new_s = s[:i] + s[i+1:]
            if len(new_s) > 1:
                if find_word(new_s, hash_table) and is_reducible(new_s, hash_table, hash_memo):
                    insert_word(s, hash_memo)
                    return True
            else:
                if is_reducible(new_s, hash_table, hash_memo):
                    insert_word(s, hash_memo)
                    return True
    return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    return sorted([word for word in string_list if len(word) == 10])


def main():
    # create an empty word_list
    word_list = []
    # open the file words.txt
    words = open('words.txt', 'r')
    # read words from words.txt and append to word_list
    for word in words:
        word_list.append(word.strip())
    # close file words.txt
    words.close()
    # find length of word_list
    n = 2 * len(word_list) + 1
    # determine prime number N that is greater than twice
    # the length of the word_list
    while not is_prime(n):
        n += 1
    # create an empty hash_list
    hash_list = ['' for i in range(n)]
    # populate the hash_list with N blank strings
    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)
    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    m = int(0.2 * len(word_list)) + 1
    while not is_prime(m):
        m += 1
    # populate the hash_memo with M blank strings
    hash_memo = ['' for i in range(m)]
    # create an empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
    # find words of length 10 in reducible_words
    reducible_words = get_longest_words(reducible_words)
    # print the words of length 10 in alphabetical order
    # one word per line
    for word in reducible_words:
        print(word)


if __name__ == "__main__":
    main()

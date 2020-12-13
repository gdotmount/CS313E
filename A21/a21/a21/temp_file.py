def grade(phrase, encode, decode):
	tree = Tree(phrase)
	try:
		encrypt = tree.encrypt(encode)
	except:
		encrypt = None
	try:
		if(encrypt != None):
			back_dec = tree.decrypt(encrypt)
		else:
			back_dec = None
	except:
		back_dec = None
	try:
		decrypt = tree.decrypt(decode)
	except:
		decrypt = None
	try:
		if(decrypt != None):
			back_enc = tree.encrypt(decrypt)
		else:
			back_enc = None
	except:
		back_enc = None
	consistent = back_enc != None and back_enc == decode and back_dec != None and back_dec == encode
	return encrypt, decrypt, consistent
#  File: BST_Cipher.py
#  Description:
#  Student Name: Gabriel M. Mount
#  Student UT EID: gmm2767
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 50845
#  Date Created: 11/15/2020
#  Date Last Modified: 11/16/2020
import sys
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.lchild = None
        self.rchild = None
class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = Node()
        self.indices = {}
        encrypt_str = encrypt_str.lower()
        for c in encrypt_str:
            if ('a' <= c <= 'z' or c == ' ') and c not in self.indices:
                current = self.insert(c)
                self.indices[c] = current
    def insert(self, ch):
        index = '*'
        if self.root.data is None:
            self.root.data = ch
            return index
        index = ''
        current = self.root
        last = current
        while current is not None:
            if ch > current.data:
                last = current
                current = current.rchild
                index += '>'
            else:
                last = current
                current = current.lchild
                index += '<'
        if ch > last.data:
            last.rchild = Node(ch)
        elif ch < last.data:
            last.lchild = Node(ch)
        return index
    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        if st == '':
            return ''
        current = self.root
        for c in st:
            if current is None:
                return ''
            elif c == '*':
                current = self.root
            elif c == '<':
                current = current.lchild
            elif c == '>':
                current = current.rchild
        return current.data if current is not None else ''
    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        result = ''
        for c in st:
            if c in self.indices:
                result += self.indices[c] + '!'
        return result[:-1]
    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        result = ''
        for param in st.split('!'):
            result += self.traverse(param)
        return result
    def __str__(self):
        def iterate(current):
            return f'{current.data} -> [{iterate(current.lchild)} | {iterate(current.rchild)}]' if current is not None else '#'
        return iterate(self.root)
def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()
    # create a Tree object
    the_tree = Tree(encrypt_str)
    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()
    # print the encryption
    print(the_tree.encrypt(str_to_encode))
    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()
    # print the decryption
    print(the_tree.decrypt(str_to_decode))
if __name__ == "__main__":
    main()

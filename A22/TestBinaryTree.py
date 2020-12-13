#  File: TestBinaryTree.py

#  Description:

#  Student Name: Gabriel M. Mount

#  Student UT EID: gmm2767

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/16/2020

#  Date Last Modified: 11/20/2020


import sys


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self, data=[]):
        self.root = None
        for node in data:
            self.insert(node)

    # insert data into the tree
    def insert(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
            return
        else:
            current = self.root
            parent = self.root
            while current is not None:
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild

            if data < parent.data:
                parent.lchild = node
            else:
                parent.rchild = node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        def recursive(node1, node2):
            if node1 is not None and node2 is not None:
                if node1.data == node2.data:
                    return recursive(node1.lchild, node2.lchild) and recursive(node1.rchild, node2.rchild)
                else:
                    return False
            else:
                return node1 == node2

        return recursive(self.root, pNode.root)

    # Prints out all nodes at the given level
    def print_level(self, level):
        def recursive(node, lev):
            if node is not None:
                if lev == 1:
                    print(node.data, end=' ')
                else:
                    recursive(node.lchild, lev - 1)
                    recursive(node.rchild, lev - 1)
        recursive(self.root, level)

    # Returns the height of the tree
    def get_height(self):
        def recursive(node, level):
            if node is None:
                return level - 1
            else:
                return max(recursive(node.lchild, level + 1), recursive(node.rchild, level + 1))
        return recursive(self.root, 1)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        def recursive(node):
            if node is None:
                return 0
            else:
                return 1 + recursive(node.lchild) + recursive(node.rchild)
        return recursive(self.root)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    tree1 = Tree(tree1_input)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    tree2 = Tree(tree2_input)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    tree3 = Tree(tree3_input)

# Test your method is_similar()
    print(f'Tree1 to Tree1: {tree1.is_similar(tree1)}')
    print(f'Tree1 to Tree2: {tree1.is_similar(tree2)}')
    print(f'Tree1 to Tree3: {tree1.is_similar(tree3)}')
    print(f'Tree1 to Blank Tree: {tree1.is_similar(Tree())}')
    print(f'Blank Tree to Blank Tree: {Tree().is_similar(Tree())}')
    print()

# Print the various levels of two of the trees that are different
    for i in range(1, tree1.get_height() + 1):
        tree1.print_level(i)
        print()
    print()
    for i in range(1, tree3.get_height() + 1):
        tree3.print_level(i)
        print()
    print()

# Get the height of the two trees that are different
    print(f'Height of Tree1: {tree1.get_height()}')
    print(f'Height of Tree3: {tree3.get_height()}')
    print()

# Get the total number of nodes a binary search tree
    print(f'Tree1 nodes: {tree1.num_nodes()}')
    print(f'Tree3 nodes: {tree3.num_nodes()}')


if __name__ == "__main__":
    main()

#  File: ExpressionTree.py

#  Description:

#  Student's Name: Gabriel M. Mount

#  Student's UT EID: gmm2767

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/13/2020

#  Date Last Modified: 11/13/2020


import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check if a stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = Node(None)
        self.operators = ['/', '//', '*', '**', '%', '+', '-']

    def is_operator(self, data):
        return data in self.operators

    def create_tree(self, expr):
        the_stack = Stack()
        current = self.root
        for token in expr:
            if token == '(':
                current.lchild = Node(None)
                the_stack.push(current)
                current = current.lchild
            elif token == ')':
                if not the_stack.is_empty():
                    current = the_stack.pop()
            elif self.is_operator(token):
                current.data = token
                the_stack.push(current)
                current.rchild = Node(None)
                current = current.rchild
            else:
                current.data = int(token)
                current = the_stack.pop()

    def evaluate(self, aNode):
        if self.is_operator(aNode.data):
            return do_the_freaking_math(self.evaluate(aNode.lchild), self.evaluate(aNode.rchild), aNode.data)
        else:
            return aNode.data


def pre_order(aNode):
    if aNode is not None:
        print(aNode.data, end=' ')
        pre_order(aNode.lchild)
        pre_order(aNode.rchild)


def post_order(aNode):
    if aNode is not None:
        post_order(aNode.lchild)
        post_order(aNode.rchild)
        print(aNode.data, end=' ')


def do_the_freaking_math(token_1, token_2, operator):
    if operator == "+":
        return token_1 + token_2
    elif operator == "-":
        return token_1 - token_2
    elif operator == "*":
        return token_1 * token_2
    elif operator == "/":
        return token_1 / token_2
    elif operator == "//":
        return token_1 // token_2
    elif operator == "%":
        return token_1 % token_2
    elif operator == "**":
        return token_1 ** token_2


def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip().split()

    # evaluate the expression and print the result
    expression_tree = Tree()
    expression_tree.create_tree(expr)
    print(f'{" ".join(expr)} = {expression_tree.evaluate(expression_tree.root)}', end='\n\n')
    # get the prefix version of the expression and print
    print('Prefix Expression: ', end=' ')
    pre_order(expression_tree.root)
    print(end='\n\n')
    # get the postfix version of the expression and print
    print('Postfix Expression: ', end=' ')
    post_order(expression_tree.root)
    print()


if __name__ == "__main__":
    main()

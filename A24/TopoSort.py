#  File: TopoSort.py

#  Description:

#  Student Name: Gabriel Mount

#  Student UT EID: gmm2767

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 11/30/2020

#  Date Last Modified: 12/02/2020


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

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    def is_in(self, v):
        return v in self.stack


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0]


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    def copy_graph(self):
        clone = Graph()
        clone.Vertices = self.Vertices
        clone.adjMat = self.adjMat
        return clone

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return i
        return -1

    def delete_vertex(self, vertexLabel):
        ind = self.get_index(vertexLabel)
        del self.Vertices[ind]
        del self.adjMat[ind]
        for i in range(len(self.Vertices)):
            del self.adjMat[i][ind]

    def delete_edge(self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)
        end = self.get_index(toVertexLabel)
        self.adjMat[start][end] = 0
        self.adjMat[end][start] = 0

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0 and not self.Vertices[i].was_visited():
                return i
        return -1

    def get_neighbors(self, vertexLabel):
        neighbors = []
        ind = self.get_index(vertexLabel)
        for i in range(len(self.Vertices[ind])):
            if self.Vertices[ind][i] != 0:
                neighbors.append(self.Vertices[ind][i])
        return neighbors

    def get_vertices(self):
        for i in range(len(self.Vertices)):
            print(self.Vertices[i])

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while not theStack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if u == -1:
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        theQueue = Queue()
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit all the other vertices according to depth
        while not theQueue.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theQueue.peek())
            if u == -1:
                u = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    def check_adj(self, stack):
        n = len(self.Vertices)
        v = stack.peek()
        for i in range(n):
            visited = self.Vertices[i].was_visited()
            edge = self.adjMat[v][i]
            if edge > 0 and visited:
                if stack.is_in(i):
                    return 0
            elif edge > 0 and not visited:
                return i
        return -1

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):
        n = len(self.Vertices)
        for v in range(n):
            stack = Stack()
            self.Vertices[v].visited = True
            stack.push(v)
            while not stack.is_empty():
                u = self.check_adj(stack)
                if u == -1:
                    u = stack.pop()
                elif u == 0:
                    n = len(self.Vertices)
                    for i in range(n):
                        self.Vertices[i].visited = False
                    return True
                else:
                    self.Vertices[u].visited = True
                    stack.push(u)
            n = len(self.Vertices)
            for i in range(n):
                self.Vertices[i].visited = False
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        g = self.copy_graph()
        visited = []
        deleted = []
        x = 0
        while len(g.Vertices) > 0:
            x = 0
            while x < len(g.Vertices):
                visitor = False
                v = g.Vertices[x]
                for i in range(len(g.Vertices)):
                    if g.adjMat[i][x] == 1:
                        visitor = True
                        break
                if visitor:
                    x += 1
                else:
                    visited.append(v)
                    deleted.append(v)
                    x += 1
            for vert in deleted:
                g.delete_vertex(vert.get_label())
            deleted = []
        return visited


def main():
    # create a Graph object
    theGraph = Graph()
    n = int(input())
    for i in range(n):
        theGraph.add_vertex(input())
    n = int(input())
    for i in range(n):
        edge = input().split()
        theGraph.adjMat[theGraph.get_index(edge[0])][theGraph.get_index(edge[1])] = 1

    # test if a directed graph has a cycle
    if theGraph.has_cycle():
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if not theGraph.has_cycle():
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print([vert.label for vert in vertex_list])


if __name__ == '__main__':
    main()

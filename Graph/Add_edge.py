class Graph:
    def __init__(self):
        self.node = []
        self.graph = []
        self.count = 0

    def insertion(self, node):

        if node not in self.node:
            self.node.append(node)
            self.count += 1

        temp = []
        for i in self.graph:
            i.append(0)
        for i in range(self.count):
            temp.append(0)
        self.graph.append(temp)

    def metrix(self):

        for i in range(self.count):
            for j in range(self.count):
                print(self.graph[i][j], end="  ")
            print()

    def addEdge(self, v1, v2):

        index1 = self.node.index(v1)
        index2 = self.node.index(v2)

        self.graph[index1][index2] = 1
        self.graph[index2][index1] = 1




obj = Graph()
lst = [23,43,2,4,2,1,22,3]
for i in lst:
    obj.insertion(i)

print(obj.node)
obj.addEdge(23, 4)
obj.metrix()


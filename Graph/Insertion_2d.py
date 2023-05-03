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

obj = Graph()
lst = [23,43,2,4,2,1,22,3]
for i in lst:
    obj.insertion(i)

print(obj.node)
obj.metrix()



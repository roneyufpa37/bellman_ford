#!/usr/bin/env python
# encoding: utf-8
import random
import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    def __init__(self):
        self.vertexs = []
        self.edges = []

    def genRandomGraph(self, vertexNum, weightMax):
        self.vertexs = range(vertexNum)
        for i in range(vertexNum):
            tmp = []
            for j in range(vertexNum):
                if i == j:
                    tmp.append(0)
                else:
                    tmp.append(random.randint(1, weightMax))
            self.edges.append(tmp)

    def printGraph(self):
        g = nx.DiGraph()
        g.add_nodes_from(self.vertexs)
        for i in range(len(self.vertexs)):
            for j in range(len(self.vertexs)):
                if self.edges[i][j] != 0 and self.edges[i][j] < 10:
                    g.add_weighted_edges_from([(i, j, self.edges[i][j])])

        nx.draw(g, with_labels = True)
        plt.savefig("pic.png")


    def shortpath(self):
        dis = [ 'E' for i in self.vertexs]
        pre = self.vertexs
        dis[0] = 0
        for e in range(len(self.vertexs)* len(self.vertexs)):
            for i in range(len(self.vertexs)):
                for j in range(len(self.vertexs)):
                    if self.edges[i][j] != 0 and dis[i] != 'E' and self.edges[i][j]<10:
                        #weight above 16 is route unreachable
                        if dis[j] == 'E' or dis[j] > dis[i] + self.edges[i][j]:
                            dis[j] = dis[i] + self.edges[i][j]
                            pre[j] = i
        print(dis)
        print(pre)


g = Graph()
g.genRandomGraph(5, 20)
#g.vertexs=[0,1,2]
#g.edges=[[0, 1, 5],[10, 0, 1], [10, 10, 0]]
g.printGraph()
g.shortpath()
plt.show()

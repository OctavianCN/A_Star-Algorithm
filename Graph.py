from Edge import Edge
from Node import Node

class Graph:
    def __init__(self,data):
        self.edges = []
        self.nodes = []
        self.__CreateGraph(data.classPositions)
        self.__DestroyUpsetsEdges(data.upsets)
    def AddEdge(self,edge):
        self.edges.append(edge)
    def RemoveEdge(self,edge):
        for ed in self.edges:
            if ed.start.info == edge.start.info and ed.end.info == edge.end.info:
                self.edges.remove(ed)
    def __CreateGraph(self,data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != "liber": #creez un nod pt fiecare nume daca nu este loc liber
                    node1 = Node(data[i][j])
                    node1.SetXYPos(i,j) #ii setez pozitia in banca
                    self.nodes.append(node1) # adaug nodul intr-o lista de noduri
                    self.__SetNodeNeighbors(node1,data,i,j) #ii setez muchiile cu vecinii
    def __SetNodeNeighbors(self,node,data,i,j):
        # Pentru fiecare verific daca pozitia vecinului este un element din clasa sau nu este un loc liber
        if i - 1 >= 0 and data[i-1][j] != "liber":
            node2 = Node(data[i-1][j])
            edge = Edge(node,node2, 1)
            self.edges.append(edge)

        if i + 1 < len(data) and data[i+1][j] != "liber":
            node2 = Node(data[i+1][j])
            edge = Edge(node,node2,1)
            self.edges.append(edge)
        #cand schimba coloana verific daca are coleg de banca in dreapta sau daca este in ultimele doua bangi
        if j - 1 >= 0 and data[i][j-1] != "liber":
            if j % 2 != 0 or i > len(data[i]) - 2: #daca sunt in ultimele 2 randuri sau au coleg de banca in dreapta
                node2 = Node(data[i][j-1])
                edge = Edge(node,node2, 1)
                self.edges.append(edge)
        if j + 1 < len(data[i]) and data[i][j+1] != "liber":
            if j % 2 == 0 or i > len(data[i])-2: #daca sunt in ultimele 2 randuri sau au coleg de banca in dreapta
                node2 = Node(data[i][j+1])
                edge = Edge(node,node2,1)
                self.edges.append(edge)



    def __DestroyUpsetsEdges(self, upsets):
        for upset in upsets: #elimin muchiile dintre perosanele suparate
            node1 = Node(upset[0])
            node2 = Node(upset[1])
            edge = Edge(node1,node2,1)
            edgeReverse = Edge(node2,node1,1)
            self.RemoveEdge(edge)
            self.RemoveEdge(edgeReverse)
    def FindNodeByName(self,name):
        for node in self.nodes:#gasesc un nod dupa nume
            if name == node.info:
                return node
    def ShowGraph(self):
        for node in self.nodes:
            print(node.info,node.xPos,node.yPos)
    def ShowEdges(self):
        for edge in self.edges:
            print(edge.start.info,edge.end.info)



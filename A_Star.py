import math

from Graph import Graph
from InputData import InputData
import time
class A_Star:

    def __init__(self,dataPath):
        inputData = InputData(dataPath)
        self.graph = Graph(inputData) # imi incarc graful
        self.openList = {}  # key = nodeName data = A*Score, GCost, cameFrom
        self.closedList = {}
        self.startNode = self.graph.FindNodeByName(inputData.messageBetween[0]) #setez nodul de start
        self.endNode = self.graph.FindNodeByName(inputData.messageBetween[1]) #setez nodul de final



    def FindPath(self,type):
        # calculez euristicile dupa tipul ales
        if type == 1:
            self.__CalculateHeuristicValues1()
        if type == 2:
            self.__CalculateHeuristicValues2()
        if type == 3:
            self.__CalculateHeuristicValues3()
        if type < 1 or type > 3:
            print("Type not in range ",1, " ",3," We will use type 1 heuristic")
            self.__CalculateHeuristicValues1() #setez ca euristica default in caz ca tipul a fost gresit euristica 1
        self.openList[self.startNode.info] = (self.startNode.hCost,0,None) #adaug in openList primul nod astfel key = numele nodului iar valoareava fi costul functiei a* costul sa se ajunga la el si parintele lui
        nr = 0
        timeStart = time.time()
        while self.openList:
            nr = nr + 1
            currentNode = self.__GetLowestFCostNodeFromOpenList() # iau nodul cu cel mai mic a*
            if self.__CheckFinal(currentNode[2]): #verific daca este nod final
               path = []
               path.append((currentNode[2],(self.graph.FindNodeByName(currentNode[2]).xPos,
                           self.graph.FindNodeByName(currentNode[2]).yPos))) #daca este il adaug intr- o liata numita cale
               cameFrom = self.openList[currentNode[2]][2] #ii iau parintele daca il are
               if cameFrom !=None:
                   position = (self.graph.FindNodeByName(cameFrom).xPos,
                               self.graph.FindNodeByName(cameFrom).yPos)
               while cameFrom != None: #cat timp nodurile au parinti iau din aproape in aproape pana la primul nod care nu are parinte acela fiind nodul de start
                   path.append((cameFrom,position))
                   cameFrom = self.closedList[cameFrom][2]
                   if cameFrom != None:
                        position = (self.graph.FindNodeByName(cameFrom).xPos,
                               self.graph.FindNodeByName(cameFrom).yPos)
               timeStop = time.time()

               t = timeStop-timeStart
               path.append((" "+str(t)+" ",(0,0)))
               print("Nr of Steps ", nr)
               return path
            del self.openList[currentNode[2]] # daca nu e stare finala il scot din lista open
            self.closedList[currentNode[2]] = (currentNode[0],currentNode[1],currentNode[3]) #il bag in lista close
            neighbors = self.__FindNeighbors(currentNode) #ii bag intr-o lista toti vecinii/succesorii
            for neighbor in neighbors:
                if neighbor in self.closedList: #verific daca vecinul este in close List si daca este ignor deoarece datorita faptului ca in cazul acestei probleme
                    continue                    # costul muchiilor este constant si pentru ca exista o muchie dus si intors pt fiecare nod cu muchii
                                                # atunci inseamna ca nu mai exista o alta cale sa se gaseasca pentru nodul curent decat pentru un  a* score mai mare
                if neighbor in self.openList: # verific daca este in openList
                    if self.openList[neighbor][0] > neighbors[neighbor][0]: #daca este si are un a* scor mai bun in bag pe vecin in openList
                        del self.openList[neighbor]
                        self.openList[neighbor] = neighbors[neighbor]
                else: #daca nu este il bag in openList
                    self.openList[neighbor] = neighbors[neighbor]
        path = []
        path.append(("Path Not Found",(0,0))) #daca nu este atunci creez un element care sa imi spuna ca nu a gasit calea
        return path



    def __GetLowestFCostNodeFromOpenList(self):
        #setez default pe cel mai mic ca primul elem din openList
        lowestFCostName = list(self.openList)[0]
        lowestFCost = self.openList[list(self.openList)[0]][0]
        lowestGCost = self.openList[list(self.openList)[0]][1]
        lowestCameFrom = self.openList[list(self.openList)[0]][2]
        for key in self.openList:
            if self.openList[key][0] < lowestFCost: # verific daca exista un nod care are a *  mai mic
                lowestFCost = self.openList[key][0]
                lowestFCostName = key
                lowestCameFrom = self.openList[key][2]
        return (lowestFCost,lowestGCost,lowestFCostName,lowestCameFrom) #returnezi caracteristicile nodului


    def __CheckFinal(self,nodeName):
        return self.endNode.info == nodeName # verific daca nodul curent are acelasi nume cu nodul final

    def __FindNeighbors(self,currentNode):
        neighbors = {}
        for edge in self.graph.edges:  #caut toate muchiile care au ca nod de start nodul timis ca parametru si bag nodul final cu caracterisicile lui intr-un dictionar de vecini
            if edge.start.info == currentNode[2]:
                name = edge.end.info
                gCost = currentNode[1] + edge.gCost
                fCost = gCost + self.graph.FindNodeByName(name).hCost
                cameFrom = edge.start.info
                neighbors[name] = (fCost,gCost,cameFrom)
        return neighbors


    def __CalculateHeuristicValues1(self):
        for node in self.graph.nodes:
            node.hCost = math.sqrt(pow(node.xPos - self.endNode.xPos, 2) +  # deoarece cel mai scurt drum este diagonale este clar ca orice alt drum este >= decat acest drum - conditie admisibilitate
                                    pow(node.yPos - self.endNode.yPos, 2))  # euristica tatalui este h(tata) = sqrt( (x-xEnd)^2 + (y-yEnd)^2) iar deoarece la euristica fiilor se aduna costul muchiei atunci fiul va avea scor mai mare ca tatal
    def __CalculateHeuristicValues2(self):
        for node in self.graph.nodes:
            node.hCost = abs(node.xPos - self.endNode.xPos) + abs(node.yPos - self.endNode.yPos)    #deoarece nu se poate deplasa in diagonala cel mai scurt drum posibil ar fi sa mergem
                                                                                                    # drept pana la pozitia in care au x egali apoi drept pana au y egali sau invers y dupa x deci
                                                                                                    #indeplineste conditia de   admisibilitate
    def __CalculateHeuristicValues3(self): # euristica neadmisibila
        lastNodeCost = 0
        nr = 0
        for node in self.graph.nodes:
            node.hCost = node.xPos + node.yPos + lastNodeCost
            lastNodeCost = node.hCost + lastNodeCost
            nr = nr + 1
            if nr == 5:
                lastNodeCost = 0
                nr = 0
            if node.xPos == 1 and node.yPos == 2:
                node.hCost = len(self.graph.edges)*len(self.graph.nodes)






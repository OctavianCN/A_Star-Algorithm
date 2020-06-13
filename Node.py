class Node:
    def __init__(self,info):
        self.info = info
        self.hCost = None
        self.xPos = None
        self.yPos = None
    def SetXYPos(self,x,y):
        self.xPos = x
        self.yPos = y

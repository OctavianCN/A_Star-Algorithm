from A_Star import A_Star
from OutputData import OutputData
import os
inputPathList = ['data/input_1.txt','data/input_2.txt','data/input_3.txt','data/input_4.txt']
outputPathList = []
nr = 1
for inputPath in inputPathList:
    outputPath = 'data/output_' + str(nr) + '.txt' #creez o cale pt fisierele de output
    if os.path.isfile(outputPath): #daca exista un fisier la acea cale il sterg
        os.remove(outputPath)
    file = open(outputPath,"x") #creez fisierul
    nr = nr + 1
    file.close()
    aStar = A_Star(inputPath)
    path = aStar.FindPath(1)
    path.reverse()
    output = OutputData(outputPath,path)
    aStar1 = A_Star(inputPath)
    path = aStar1.FindPath(2)
    path.reverse()
    output = OutputData(outputPath, path)
    aStar2 = A_Star(inputPath)
    path = aStar2.FindPath(3)
    path.reverse()
    output = OutputData(outputPath, path)
    #adaug in fisier fiecare output pt fiecare euristica



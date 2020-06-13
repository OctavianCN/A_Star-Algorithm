class InputData:

    def __init__(self,path):
        self.classPositions=[]
        self.upsets = []
        self.messageBetween = ();
        self.__config_data(path)

    def __config_data(self, path):
        if isinstance(path, str):
            f = open(path, 'r',encoding="utf8")
            AllData=f.readlines() #citesc datele si le impart in diferite liste
            dataReadStage = 0
            for val in AllData:
                splitValues = val.split()
                if splitValues[0] == "suparati":
                    dataReadStage = 1
                elif splitValues[0] == "mesaj:":
                    dataReadStage = 2
                if dataReadStage == 0:
                    self.classPositions.append(splitValues)
                elif dataReadStage == 1:
                    if len(splitValues) == 2:
                        self.upsets.append((splitValues[0],splitValues[1]))
                elif dataReadStage == 2:
                    self.messageBetween = (splitValues[1],splitValues[3])
                f.close()

        else:
            print(path, "is not a string")
    def data_position(self,info):
        for i in range(len(self.classPositions)):
            for j in range(len(self.classPositions[i])):
                if info == self.classPositions[i][j]:
                    return i,j
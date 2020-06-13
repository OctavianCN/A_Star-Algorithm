class OutputData:
    def __init__(self, path,output):
        self.path = path
        self.content = output
        self.__WriteOutput()

    def __WriteOutput(self):
        if isinstance(self.path, str):
            f = open(self.path, 'a')
        else:
            print(self.path, "is not a string")
        lastPos = None
        nr = 0
        for val, pos in self.content:
            if lastPos != None and nr >= 2:
                if lastPos[1] != pos[1]: # daca  s-a schimbat randul
                    if pos[1] % 2 == 0: # vad pozitia randului daca este para
                        if pos[1] > lastPos[1]: # daca este para atunci inseamna ca ori
                            f.write(" >> ")         # a dat biletul pe alt culoar ori l-a
                        else:                   # dat inapoi
                            f.write(" < ")
                    else:
                        if pos[1] > lastPos[1]:
                            f.write(" > ")  #daca nu este para atunci l-a dat colegului de banca
                        else:
                            f.write(" << ") #sau l-a dat inapoi pe celalalt rand
                elif lastPos[0] != pos[0]: #verific daca au dat biletul in fata sau in spate
                    if lastPos[0] < pos[0]: #daca au dat biletul in spate
                        f.write(" V ")
                    else: #daca au dat biletul in fata
                        f.write(" ^ ")
            nr = nr + 1
            f.write(val)
            lastPos = pos
        f.write("\n")
        f.close()


import copy

class Ruch:
    def __init__(self,pozycja, pola):
        self.pozycja = pozycja
        self.pola = pola
        self.wielkoscMapy = [len(pola)-1,len(pola[0])-1]
        self.mozliweAkcje =  []
        self.tabPrawdopodobienstwo = [ [0] * (self.wielkoscMapy[1]+1) for _ in range((self.wielkoscMapy[0])+1)]
        self.potencial = 0
        self.indeksprzejsicia = [['Wdół',False,[]],['Wgóre',False,[]],['Wlewo',False,[]],['Wprawo',False,[]],['Zostaje',False,[]]]

    def ruchGora(self):
        self.nazwa = 'Góra'
        #DoPrzodu
        if self.pozycja[0]==0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')

        elif self.pola[self.pozycja[0]-1][self.pozycja[1]].typPola == 0: #przeszkoda
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wgóre')
            self.tabPrawdopodobienstwo[self.pozycja[0]-1][self.pozycja[1]] = 0.8
            self.inekdowaniePrzejsc(self.pozycja[0]-1,self.pozycja[1],'Wgóre')

        #Wlewo
        if self.pozycja[1]==0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]][self.pozycja[1]-1].typPola == 0: #przeszkoda
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wlewo')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]-1] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1]-1,'Wlewo')

        # Wprawo
        if self.pozycja[1] == self.wielkoscMapy[1]:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]][self.pozycja[1] + 1].typPola == 0: #przeszkoda
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wprawo')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1] + 1] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1] +1,'Wprawo')

    def ruchPrawo(self):
        self.nazwa = 'Prawo'
        #DoPrzodu
        if self.pozycja[1]==self.wielkoscMapy[1]:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]][self.pozycja[1]+1].typPola == 0:  #przeszkoda
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wprawo')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]+1] = 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1]+1,'Wprawo')
        #Wlewo
        if self.pozycja[0]==0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]-1][self.pozycja[1]].typPola == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wgóre')
            self.tabPrawdopodobienstwo[self.pozycja[0]-1][self.pozycja[1]] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0]-1,self.pozycja[1],'Wgóre')

        # Wprawo
        if self.pozycja[0] == self.wielkoscMapy[0]:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]+1][self.pozycja[1]].typPola == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wdół')
            self.tabPrawdopodobienstwo[self.pozycja[0]+1][self.pozycja[1]] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0]+1,self.pozycja[1],'Wdół')

    def ruchDol(self):
        self.nazwa = 'Dół'
        # DoPrzodu
        if self.pozycja[0] == self.wielkoscMapy[0]:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]+1][self.pozycja[1]].typPola == 0:  # przeszkoda
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wdół')
            self.tabPrawdopodobienstwo[self.pozycja[0]+1][self.pozycja[1]] = 0.8
            self.inekdowaniePrzejsc(self.pozycja[0]+1,self.pozycja[1],'Wdół')
        # Wlewo
        if self.pozycja[1] == self.wielkoscMapy[1]:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]][self.pozycja[1]+1].typPola == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wprawo')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]+1] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1]+1,'Wprawo')
        # Wprawo
        if self.pozycja[1] == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]][self.pozycja[1]-1].typPola == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wlewo')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]-1] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1]-1,'Wlewo')

    def ruchLewo(self):
        self.nazwa = 'Lewo'
        # DoPrzodu
        if self.pozycja[1] == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]][self.pozycja[1]-1].typPola == 0:  # przeszkoda
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wlewo')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]-1] = 0.8
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1]-1,'Wlewo')
        # Wlewo
        if self.pozycja[0] == self.wielkoscMapy[0]:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]+1][self.pozycja[1]].typPola == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wdół')
            self.tabPrawdopodobienstwo[self.pozycja[0]+1][self.pozycja[1]] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0]+1,self.pozycja[1],'Wdół')
        # Wprawo
        if self.pozycja[0] == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        elif self.pola[self.pozycja[0]-1][self.pozycja[1]].typPola == 0:
            self.mozliweAkcje.append('Zostaje')
            self.tabPrawdopodobienstwo[self.pozycja[0]][self.pozycja[1]] += 0.1
            self.inekdowaniePrzejsc(self.pozycja[0],self.pozycja[1],'Zostaje')
        else:
            self.mozliweAkcje.append('Wgóre')
            self.tabPrawdopodobienstwo[self.pozycja[0]-1][self.pozycja[1]] = 0.1
            self.inekdowaniePrzejsc(self.pozycja[0]-1,self.pozycja[1],'Wgóre')

    def inekdowaniePrzejsc(self,poz1,poz2,indexTxt):
        temp = [poz1,poz2]
        ind = self.znajdzIndeks(indexTxt)
        self.indeksprzejsicia[ind][2] = temp 
        self.indeksprzejsicia[ind][1] = True

    def znajdzIndeks(self,indexTxt):
        for indexe, element in enumerate(self.indeksprzejsicia):
            if element[0] == indexTxt:
               return indexe
        return 'error'

    def obliczPotencialAkcji(self):
        self.potencial = 0
        for element in self.indeksprzejsicia:
            if element[1]:
               self.potencial += copy.copy(self.tabPrawdopodobienstwo[element[2][0]][element[2][1]])*self.pola[element[2][0]][element[2][1]].potencial



from Pole import *

class Bellman:
  tablicaObjektowPol = []
  pola = [[]]
  def __init__(self, gamma, kroki):
    self.gamma = gamma
    self.kroki = kroki
  def mapa(self,plik_mapy):
    with open(plik_mapy) as plik:
        for wiersze in plik:
            w = []
            for kolumny in wiersze.split():
                w.append(kolumny)
            self.pola.append(w)
    self.ileKolumn = int(self.pola[1][0])
    self.ileWierszy = int(self.pola[1][1])
  def wyswietlMape(self):
      print(self.pola)
  def mapaJakoTablicaPol(self):
      self.polaDoSprawdzenia = []
      for indeks, poleW in enumerate(self.pola):
          if (indeks > 1) and ((self.ileKolumn+1) > indeks):
              wiersz = []
              for indeksK, poleK in enumerate(poleW):
                    pole = Pole(int(poleK),[indeks-2,indeksK])
                    if int(poleK) == 1:
                        self.polaDoSprawdzenia.append([indeks-2,indeksK])
                    pole.przypiszNagrode(int(self.pola[indeks+4][indeksK]))
                    wiersz.append(pole)
              self.tablicaObjektowPol.append(wiersz)
              wiersz = []
  def prawdopodobienstwaPol(self):
      for wiersz in self.tablicaObjektowPol:
          for element in wiersz:
              element.obliczPrawdopodobienstwo(self.tablicaObjektowPol)
  
  def algorytm(self):
      self.mapaJakoTablicaPol()
      self.prawdopodobienstwaPol()


      for i in range(0,self.kroki):
          for wiersz in self.tablicaObjektowPol:             
              for element in wiersz:
                  if (element.typPola == 1) and (element.indeks in self.polaDoSprawdzenia):
                     najlepszyRuchPotencial = element.wybierzNajlepszyRuch()
                     temp = element
                     nowaWartosc = temp.nagroda + self.gamma * najlepszyRuchPotencial
                     if element.przestanSprawdzac(nowaWartosc):
                        self.polaDoSprawdzenia.remove(element.indeks)
                        continue                     
                     temp.potencial = nowaWartosc
  def wyswietlWynik(self):
        mapa = 'Mapa potencjałów'
        new_mapa = mapa.center(74)
        polityka = 'Polityka ruchów'
        new_polityka = polityka.center(74)
        print('', new_mapa + '\n\n')
        for wiersz in self.tablicaObjektowPol:
              wynik = ''
              new_wynik = wynik.center(24)
              for element in wiersz:
                  new_wynik += str(round(element.potencial,2)) + '\t'
              print (new_wynik +'\n\n')
        print ('', new_polityka + '\n\n')
        for wiersz in self.tablicaObjektowPol:
              wynik = ''
              new_wynik = wynik.center(26)
              for element in wiersz:
                  new_wynik += str(element.ruchNajlepszy()) + '\t'
              print (new_wynik +'\n')

                 
      
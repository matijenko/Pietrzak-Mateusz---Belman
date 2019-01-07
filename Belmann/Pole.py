from Ruch import *

class Pole:
  def __init__(self, typPola, indeks):
      self.typPola = typPola
      self.indeks = indeks
      self.ruchy = []
      self.najlepszyRuch = 'Góra'

  def przypiszNagrode(self, nagroda):
    self.nagroda = nagroda
    self.potencial = nagroda

  def obliczPrawdopodobienstwo(self,pola):
      rg = Ruch(self.indeks,pola)
      rg.ruchGora()
      self.ruchy.append(rg)

      rp = Ruch(self.indeks, pola)
      rp.ruchPrawo()
      self.ruchy.append(rp)

      rd = Ruch(self.indeks, pola)
      rd.ruchDol()
      self.ruchy.append(rd)

      rl = Ruch(self.indeks, pola)
      rl.ruchLewo()
      self.ruchy.append(rl)

  def wybierzNajlepszyRuch(self):
      max = 0
      for ruch in self.ruchy:
          ruch.obliczPotencialAkcji()

      for indexe,element in enumerate(self.ruchy):
          if (indexe==0):
             max = element.potencial
             self.najlepszyRuch = element.nazwa
             continue
          if max<element.potencial:
             max = element.potencial
             self.najlepszyRuch = element.nazwa
      return max
 
  def przestanSprawdzac(self,nowaWartosc):
      if 0.000000001 >abs(self.potencial-nowaWartosc):
          return True
      return False
  def ruchNajlepszy(self):
      if self.typPola == 0 or self.typPola == 2: 
        return 0
      if self.najlepszyRuch == 'Góra': 
        return 1
      if self.najlepszyRuch == 'Prawo': 
        return 2
      if self.najlepszyRuch == 'Dół': 
        return 3
      if self.najlepszyRuch == 'Lewo': 
        return 4
      
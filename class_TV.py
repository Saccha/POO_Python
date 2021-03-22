"""
3. Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""
class Televisao():
 def __init__(self):
  self.setCanal(0)
  self.volume = 2
 def setCanal(self, canal):
  if (canal > 0) and (canal <= 100):
    self.canal = canal
 def aumentarVolume(self):
  if (self.volume < 100):
    self.volume += 1
 def diminuirVolume(self):
  if (self.volume > 0):
    self.volume -= 1
#Programa Principal
tv = Televisao()
print(vars(tv))
tv.setCanal(12)
print(vars(tv))
tv.aumentarVolume()
print(vars(tv))
tv.diminuirVolume()
print(vars(tv))

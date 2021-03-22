"""
2. Crie uma classe que representa um retângulo. Em seguida, crie um
programa principal que utilize esta classe. O programa deve pedir ao usuário que
informe as medidas dos dois lados de um retângulo. Depois deve criar um objeto com
essas medidas e exibir sua  ́area e seu perímetro.
"""

class Retangulo():
  def __init__ (self,ladoA, ladoB):
    self.ladoA = ladoA
    self.ladoB = ladoB
  def mudarLados(self,ladoA, ladoB):
    if ladoA > 0:
      self.ladoA = ladoA
    if ladoB > 0:
      self.ladoB = ladoB
  def retornarLados (self):
    return (self.ladoA,self.ladoB)
  def calcularArea (self):
    return self.ladoA*self.ladoB
  def calcularPerimetro (self):
    return (self.ladoA*2)+(self.ladoB*2)
    
#Programa principal
lado1 = int(input("informe o lado A: "))
lado2 = int(input("informe o lado B: "))
R1 = Retangulo(lado1,lado2)
area = R1.calcularArea()
print("A qtde de azuleijos e: " + str(area/2))

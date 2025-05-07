class Persona:
  def __init__(self,Nombre,Apellido,Numero_de_documento,Ano_de_Nacimiento):
    self.Nombre = Nombre
    self.Apellido = Apellido
    self.Numero_de_documento = Numero_de_documento
    self.Ano_de_Nacimiento = Ano_de_Nacimiento

  def imprimir(self):
    print("Nombre:", self.Nombre)
    print("Apellido:", self.Apellido)
    print("Numero_de_documento:", self.Numero_de_documento)
    print("Ano_de_Nacimiento:", self.Ano_de_Nacimiento)
    print()

Persona_1 = Persona("Santiago", "Romero", "1007739222", 2001)
Persona_2 = Persona("Berena", "Arroyo", "1007739227", 2001)

Persona_1.imprimir()
Persona_2.imprimir()

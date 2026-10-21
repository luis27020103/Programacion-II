class CriaturaMarina:
    def __init__(self, nombre):
        self.nombre = nombre
    def metodo1(self):
        print("criatura 1")

    def metodo2(self):
        print("criatura 2")
    def __str__(self):
        return "criatura marina " + self.nombre
class Mamifero(CriaturaMarina):
    def __init__(self, nombre):
        super().__init__(nombre)

    def metodo1(self):
        print("sangre caliente")

    def __str__(self):
        return "mamifero " + self.nombre
class Delfin(Mamifero):
    def __init__(self, nombre):
        super().__init__(nombre)
    def metodo1(self):
        print("sopla burbujas")
        super().metodo1()
    def __str__(self):
        return "delfin " + self.nombre
class Calamar(CriaturaMarina):
    def __init__(self, nombre):
        super().__init__(nombre)
    def metodo2(self):
        print("tentáculos")
    def __str__(self):
        return "calamar " + self.nombre
class Ballena(Mamifero):
    def __init__(self, nombre):
        super().__init__(nombre)
    def metodo1(self):
        print("canta canciones")
    def __str__(self):
        return "ballena " + self.nombre
    def nadar(self):
        print("nada profundamente")
elementos = [
    Calamar("Calamardo"),
    Delfin("Flipper"),
    Mamifero("Moby"),
    CriaturaMarina("Marina"),
    Ballena("Willy")
]
for i in range(len(elementos)):
    elementos[i].metodo2()
    print(elementos[i])
    elementos[i].metodo1()
    print()
ballena = Ballena("Willy")
ballena.nadar()
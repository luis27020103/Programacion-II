import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
        self.vidasIniciales = numeroDeVidas
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
    def actualizaRecord(self):
        self.record += 1
        print("Nuevo record:", self.record)
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            return True
        else:
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.randint(0, 10)
        print("Adivina un numero entre 0 y 10")
        while True:
            numero = int(input("Introduce un numero: "))
            if numero == self.numeroAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                quedanVidas = self.quitaVida()
                if quedanVidas:
                    print("Vida perdida")
                    print("Te quedan", self.numeroDeVidas, "vidas")
                    print("Intenta de nuevo")
                else:
                    print("No te quedan mas vidas")
                    print("El numero era:", self.numeroAdivinar)
                    print("Fin del juego")
                    break
# CLASE APLICACION
if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)
    juego.juega()
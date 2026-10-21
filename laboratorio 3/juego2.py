from juego1 import Juego, JuegoAdivinaNumero
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10 and numero % 2 == 0:
            return True
        else:
            print("Error: el numero debe ser par y estar entre 0 y 10")
            return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10 and numero % 2 != 0:
            return True
        else:
            print("Error: el numero debe ser impar y estar entre 0 y 10")
            return False
class Aplicacion:
    def main(self):
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)
        print("JUEGO ADIVINA NUMERO")
        juego1.juega()
        print("\nJUEGO ADIVINA PAR")
        juego2.juega()
        print("\nJUEGO ADIVINA IMPAR")
        juego3.juega()
if __name__ == "__main__":
    app = Aplicacion()
    app.main()
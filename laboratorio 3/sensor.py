class Sensor:
    tipo = "Generico"
    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.encendido = False
    def activar(self):
        self.encendido = True
        print("Sensor activado")
    def desactivar(self):
        self.encendido = False
        print("Sensor desactivado")
class Camara(Sensor):
    tipo = "Camara"
    def __init__(self, id, resolucion, **kwargs):
        self.resolucion = resolucion
        super().__init__(id=id, **kwargs)
class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"
    def __init__(self, id, alcance, **kwargs):
        self.alcance = alcance
        super().__init__(id=id, **kwargs)
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehiculo Autonomo"
    def __init__(self, id, resolucion, alcance):
        super().__init__(
            id=id,
            resolucion=resolucion,
            alcance=alcance
        )
if __name__ == "__main__":
    vehiculo = VehiculoAutonomo(
        "VA001",
        "4K",
        200
    )
    print("Tipo:", vehiculo.tipo)
    print("ID:", vehiculo.id)
    print("Resolucion:", vehiculo.resolucion)
    print("Alcance:", vehiculo.alcance)
    print("Encendido:", vehiculo.encendido)
    vehiculo.activar()
    print("Encendido:", vehiculo.encendido)
    vehiculo.desactivar()
    print("Encendido:", vehiculo.encendido)
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "amarillo" or color == "verde" or color == "rojo" or color == "negro" or color == "blanco":
            self.color = color
             
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, marca, registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = None
        self.registro = registro
        self.asientos = None
    
    asientos = Asiento()
    motor = Motor()

    def cantidadAsientos(self):
        cont = 0
        for i in range(self.asientos):
            if self.asientos[i].type == Asiento:
                cont += 1
        
        return cont

    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for i in range(self.asientos):
                if self.asientos[i].registro == self.registro:
                    print("Auto original")
                else:
                    print("Las piezas no son originales")    
        else:
            print("Las piezas no son originales")
        
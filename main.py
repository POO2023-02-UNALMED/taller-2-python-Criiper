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
    def __init__(self, modelo, precio, marca, asientos, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.asientos = asientos
        
    def cantidadAsientos(self):
        cont = 0
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                cont += 1
        
        return cont

    def verificarIntegridad(self, a):
        if self.motor.registro == self.registro:
            self.registro = a
            for i in range(len(self.asientos)):
                if self.asientos[i].registro != a:
                    return("Las piezas no son originales")
                    
                else:
                    return("Auto original")    
        else:
            return("Las piezas no son originales")
        
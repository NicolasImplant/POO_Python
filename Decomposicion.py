#Decomposicion

class Automovil:
    def __init__(self, modelo, marca, color, transmision):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en reposo"
        self._motor = Motor(cilindros=4)
        self.transmision = Transmision(mecanica=True, automatica=False)


    def acelerar(self, tipo = "despacio"):
        if tipo == "rapida":
            self._motor.inyecta_gasolina(10)
            self.transmision.hibridar(1)
        else:
            self._motor.inyecta_gasolina(3)
            self.transmision.hibridar(0)

        self.estado = "en movimiento"    


class Motor:
    def __init__(self,cilindros,tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self,cantidad):
        pass

class Transmision:
    def __init__(self,mecanica,automatica):
        self.mecanica = mecanica
        self.automatica = automatica
    
    def hibridar(self,cambio):
        if cambio == 1:
            self.transmision (automatica=True)
        else:
            self.transmision (mecanica=True)





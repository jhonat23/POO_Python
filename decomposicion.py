class Automovil:
    def __init__(self, modelo, marca, color) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'reposo' #variable privada: no es necesario mostrarle esto a quien use esta clase
        self._motor = Motor(cilindros=4)
        self.radio = 'apagado'
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en movimiento'

class Motor:
    def __init__(self, cilindros, tipo='gasolina', encendido = False) -> None:
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self.encendido = encendido
    
    def inyecta_gasolina(self, cantidad=0):
        pass

class Radio:
    def __init__(self) -> None:
        self.emisora = 'FM'
        self.volumen = 0
        self.on_off = False
    
    def encender_radio(self, encendido):
        if Motor.inyecta_gasolina > 1:
            self.on_off = True
            self.volumen = 5
class Lavadora:
    def __init__(self) -> None:
        pass

    def lavar(self, temperatura= 'caliente'):#esta es la "interfaz"
        self._llenar_tanque_de_agua(temperatura)#puedo definir un método dentro de otro método
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua a {temperatura}°C')
    def _anadir_jabon(self):
        print('Anadiendo jabon')
    def _lavar(self):
        print('Lavando la ropa')
    def _centrifugar(self):
        print('Centrigunado la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
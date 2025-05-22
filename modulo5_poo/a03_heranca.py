class Carro:
    numero_portas = 5
    quantidade_passageiros = 4
    
    #* metodos
    def acelerar(self):
        print('Acelerando...')
        
    def frear(self):
        print('Freando...')
        
    def buzinar(self):
        print('bi biiiiiiii')
        
class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992
    
#* Instancias
uno = Uno()
print(uno.marca)
uno.acelerar()
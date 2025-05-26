class Animal:
    def emitir_som(self):
        print('som de animal')
        
class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au!')
        
class Gato(Animal):
    def emitir_som(self):
        print('Miau!')
        
animal = Animal()
animal.emitir_som()

cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()
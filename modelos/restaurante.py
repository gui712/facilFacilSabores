class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'    

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria}')    




restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Gato Veio','Pizza')

Restaurante.listar_restaurantes()

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'    

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(22)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(22)} | {restaurante._categoria.ljust(22)} | {restaurante.ativo}')    

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'


    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Gato Veio','Pizza')


Restaurante.listar_restaurantes()


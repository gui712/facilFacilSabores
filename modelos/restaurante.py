from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'    

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(22)} | {"Status".ljust(22)} | {"Avaliação"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(22)} | {restaurante._categoria.ljust(22)} | {restaurante.ativo.ljust(22)} | {restaurante.media_avaliacoes}')    

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'


    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if nota > 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media




from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Restaurante da Praça', 'Tradicional')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.receber_avaliacao('Guilherme', 10)
restaurante_praca.receber_avaliacao('Jessica', 8)
restaurante_praca.receber_avaliacao('João', 4)

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
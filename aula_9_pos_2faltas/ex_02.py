

import datetime
import unittest

# 1. O cartão deve ter saldo maior do R$ 4.00
# 2. O cartão deve ser da mesma concessionária
#       da catraca
# 3. O cartão deve estar dentro da validade

PRECO_DA_PASSAGEM = 110.00

class SaldoInsuficienteError(Exception):
    pass

class ConcessionariaDiferenteError(Exception):
    pass

def daqui_um_ano():
    return datetime.datetime.now() + datetime.timedelta(365)

class Catraca:

    def __init__(self, concessionaria):
        self.concessionaria = concessionaria
        self.estado = 'travada'

class Cartao:

    def __init__(self, saldo, concessionaria):
        self.saldo = saldo
        self.concessionaria = concessionaria
        self.validade = daqui_um_ano()

def liberar_catraca(catraca, cartao):
    catraca.estado = 'travada'
    if cartao.saldo < PRECO_DA_PASSAGEM:
        raise SaldoInsuficienteError()
    if cartao.concessionaria != catraca.concessionaria:
        raise ConcessionariaDiferenteError()
    catraca.estado = 'liberada'

class Teste(unittest.TestCase):

    def test_fluxo_feliz(self):
        cartao = Cartao(PRECO_DA_PASSAGEM, 'sptrans')
        catraca = Catraca('sptrans')
        liberar_catraca(catraca, cartao)
        self.assertEqual(catraca.estado, 'liberada')

    def test_saldo_insuficiente(self):
        cartao = Cartao(PRECO_DA_PASSAGEM - 1.00, 'sptrans')
        catraca = Catraca('sptrans')
        with self.assertRaises(SaldoInsuficienteError):
            liberar_catraca(catraca, cartao)
        self.assertEqual(catraca.estado, 'travada')

    def test_concessionaria_diferente(self):
        cartao = Cartao(PRECO_DA_PASSAGEM, 'sptrans')
        catraca = Catraca('EMTU')
        with self.assertRaises(ConcessionariaDiferenteError):
            liberar_catraca(catraca, cartao)
        self.assertEqual(catraca.estado, 'travada')
    
    def test_saldo_insuficiente_catraca_liberada(self):
        cartao = Cartao(PRECO_DA_PASSAGEM - 1.00, 'sptrans')
        catraca = Catraca('sptrans')
        catraca.estado = 'liberada' 
        with self.assertRaises(SaldoInsuficienteError):
            liberar_catraca(catraca, cartao)
        self.assertEqual(catraca.estado, 'travada')

if __name__ == '__main__':
    unittest.main()
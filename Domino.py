from random import *

pedras = [[(0,0)],
        [(0,1),(1,1)],
        [(0,2),(1,2),(2,2)],
        [(0,3),(1,3),(2,3),(3,3)],
        [(0,4),(1,4),(2,4),(3,4),(4,4)],
        [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)],
        [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)]]


norte = []
sul = []
leste = []
oeste = []

def removeDaLinhaPedras(pedra, linha):
    pedras[linha].remove(pedra)

def removeLinhaPedras(linha):
    pedras.remove(pedras[linha])

def adquirirPedra():

    pedra = []
    tamLinha = len(pedras)
    linha = randrange(0,tamLinha)
    tamColuna = len(pedras[linha])
    coluna = randrange(0,tamColuna)
    pedra = pedras[linha][coluna]
    removeDaLinhaPedras(pedra, linha)

    if (len(pedras[linha]) == 0):
        removeLinhaPedras(linha)

    print "linha -> ",linha, " ;coluna -> ", coluna
    print "Pedras restantes -> ", pedras, "\n"

    return pedra


def distribuiPedras(qtdJogadores):

    return list( map( lambda x: map( lambda x: adquirirPedra(), range(7)), range(qtdJogadores)))


qtdJogadores = input()

maos = distribuiPedras(qtdJogadores)

print "Pedras que cada jogador possui:"

for i in range(qtdJogadores):
    print "    Jogador ", i+1 , " -> ", maos[i]

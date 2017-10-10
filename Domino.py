from random import *

pedras = [(0,0),
        (0,1),(1,1),
        (0,2),(1,2),(2,2),
        (0,3),(1,3),(2,3),(3,3),
        (0,4),(1,4),(2,4),(3,4),(4,4),
        (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),
        (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)]


lados = [0,0,0,0] # norte = 0; leste = 1; sul = 2; oeste = 3;


#def removeLinhaPedras(linha):
#    pedras.remove(pedras[linha])

def adquirirPedra():
    
    indice = randrange(0,len(pedras))
    #print "indice -> ", indice, "\n"
    pedra = pedras[indice]
    pedras.pop(indice)

    #if (len(pedras[linha]) == 0):
   #     removeLinhaPedras(linha)

    print "pedra ->", pedra, "\n"
    print "Pedras restantes -> ", pedras, "\n"

    return pedra


def distribuiPedras(qtdJogadores):

    return list( map( lambda x: map( lambda x: adquirirPedra(), range(7)), range(qtdJogadores)))


qtdJogadores = input()

maos = distribuiPedras(qtdJogadores)

def printPedras():
    print "Pedras que cada jogador possui:"

    for i in range(qtdJogadores):
        print "    Jogador ", i+1 , " -> ", maos[i]


jogadorAtual = 0
jogada = (6,6,-1)
listaPossiveisJogadas = [jogada]
qtdPassesSeguidos = 0


def fazJogada(pedra, lado):
    global lados
    maos[jogadorAtual].remove(pedra)

    if lado == -1:
        lados = [6,6,6,6]
    else:
        x,y = pedra
        if x == lados[lado]:
            lados[lado] = y
        else:
            lados[lado] = x


def possiveisJogadas():
    global listaPossiveisJogadas
    global lados
    listaPossiveisJogadas = []

    for i in range(4):
        for pedra in maos[jogadorAtual]:
            x, y = pedra

            if x == lados[i] or y == lados[i]:
                listaPossiveisJogadas.append((x,y,i))


def escolheJogada():
    global jogada
    jogada = listaPossiveisJogadas[randrange(0, len(listaPossiveisJogadas))]


def fazPrimeiraJogada():
    global jogadorAtual
    global jogada
    encontrouPedra6_6 = False
    j = 0

    while jogadorAtual < qtdJogadores and not encontrouPedra6_6:
        j = 0

        while j < 7 and not encontrouPedra6_6:
            if (maos[jogadorAtual][j] == (6,6)):
                encontrouPedra6_6 = True
            else:
                j += 1

        if not encontrouPedra6_6:
            jogadorAtual += 1

    x,y,lado = jogada
    printPartida()
    fazJogada((x,y), lado)
    defineJogadorAtual()


def defineJogadorAtual():
    global jogadorAtual

    if (jogadorAtual + 1 == 4):
        jogadorAtual = 0
    else:
        jogadorAtual += 1


def verificaFimPartida():
    return (verificaPassesSeguidos() or verificaSeExisteMaoVazia())


def verificaPassesSeguidos():
    return (qtdPassesSeguidos == qtdJogadores)


def verificaSeExisteMaoVazia():
    for i in range(qtdJogadores):
        if len(maos[i]) == 0:
            return True

    return False


def printPartida():
    print "\n___________________________________________________________\nJogador ", jogadorAtual+1, " realiza jogada:\n   Mao -> ", maos[jogadorAtual], "\n   Possiveis jogadas -> ", listaPossiveisJogadas, "\n   Jogada -> ", jogada, "\n\nDados da Partida:\n   Quantidade de passes seguidos -> ", qtdPassesSeguidos, "\n   Lados da mesa -> Norte ==>",lados[0],"\n                    Leste ==>",lados[1],"\n                    Sul   ==>",lados[2],"\n                    Oeste ==>",lados[3]


def prepararPartida():
    global pedras
    global lados
    global maos
    global jogadorAtual
    global jogada
    global listaPossiveisJogadas
    global qtdPassesSeguidos

    pedras = [(0,0),
            (0,1),(1,1),
            (0,2),(1,2),(2,2),
            (0,3),(1,3),(2,3),(3,3),
            (0,4),(1,4),(2,4),(3,4),(4,4),
            (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),
            (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)]

    lados = [0,0,0,0] # norte = 0; leste = 1; sul = 2; oeste = 3;

    maos = distribuiPedras(qtdJogadores)

    jogadorAtual = 0
    jogada = (6,6,-1)
    listaPossiveisJogadas = [jogada]
    qtdPassesSeguidos = 0


def partida():
    global qtdPassesSeguidos
    partidas = 0
    totalPasses = 0
    qtdAcabouPorPasses = 0

    while partidas < 1000:
        prepararPartida()
        fazPrimeiraJogada()
        possiveisJogadas()

        while (not verificaFimPartida()):
            printPartida()

            if len(listaPossiveisJogadas) > 0:
                escolheJogada()
                x,y,lado = jogada
                fazJogada((x,y), lado)
                qtdPassesSeguidos = 0

            else:
                qtdPassesSeguidos += 1
                totalPasses += 1
                if qtdPassesSeguidos == qtdJogadores:
                    qtdAcabouPorPasses += 1

            defineJogadorAtual()
            possiveisJogadas()

        partidas += 1

    print "\npartidas -> ", partidas
    print "Total de passes -> ", totalPasses
    print "Quantidade de vezes que a partida acabou por ninguem ter uma jogada possivel -> ", qtdAcabouPorPasses


partida()

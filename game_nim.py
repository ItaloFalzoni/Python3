tipo_jogo = 0
 
def computador_escolhe_jogada(n, m):
    print()
    if n <= m:
        return n
    else:
        quantia = n % (m + 1)
        if quantia > 0:
            return quantia
        return m

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        print()
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            print("\nOops! Jogada inválida! Tende de novo.")
            jogada = 0
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    comeca_computador = True
    if n % m == 1:
        comeca_computador = False
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
    while n > 0:
        if comeca_computador:
            jogada = computador_escolhe_jogada(n, m)
            comeca_computador = False
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            comeca_computador = True
            if jogada == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("\nVocê tirou {} peças.".format(jogada))
        n = n - jogada
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n != 0:
            print("Agora restam {} peças no tabuleiro.".format(n))
    if comeca_computador:
        print("Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0
 
def campeonato():
    usuario = 0
    computador = 0
    for x in range(3):
        print("\n**** Rodada",x + 1,"****\n")
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))
while tipo_jogo == 0:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")
    tipo_jogo = int(input("Sua opção: "))
    print(" ")
    if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
    if tipo_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opção inválida!")
        tipo_jogo = 0

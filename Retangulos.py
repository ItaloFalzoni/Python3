i = 0

def retangulo_vazado():
    print ("\nVocê escolheu Retângulo Vazado.")
    largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))

    print("#" * largura)
    for _ in range(altura - 2):
        print("#" + " " * (largura - 2) + "#")
    print("#" * largura)
    return ""

def retangulo_cheio():
    print ("\nVocê escolheu Retângulo Preenchido.")
    repetir_largura = largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))
    while altura > 0:
        while largura > 0:
            print ("#",end='')
            largura = largura - 1
        print ()
        largura = repetir_largura
        altura = altura - 1
    return ""

print ("Bem vindo ao criador de retângulos simulados.")
while i < 1:
    print ("Escolha um tipo:")
    print ("1 - Retângulo preenchido.")
    print ("2 - Retângulo Vazado.")
    print ("0 - Sair.")
    escolha = int(input("Sua escolha: "))

    if escolha == 1:
        print (retangulo_cheio())
    elif escolha == 2:
        print (retangulo_vazado())
    elif escolha == 0:
        print ("\nVocê escolheu sair.")
        print ("\nFim do programa.")
        i = 1
    else:
        print ("\nEscolha um valor válido.\n")

from random import choice
lista=['R','T','P']
pontuacao_maquina=pontuacao_usuario=0
while True:
    print('-'*60)
    print('Pedra, Papel e Tesoura'.center(60))
    print('-'*60)
    escolha=str(input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou S para sair: ")).upper().strip()
    while escolha!='R' and escolha!='T' and escolha!='P' and escolha!='S':
        escolha=str(input("Valor Indefinido!!!\nEscolha R(Pedra)/T(Tesoura)/P(Papel) ou S para sair: ")).upper().strip()
    if escolha == 'S':    
        print(f"Sua pontuação: {pontuacao_usuario}\nPontuação da máquina: {pontuacao_maquina}")
        if pontuacao_usuario>pontuacao_maquina:
            print("VOCÊ GANHOU")
        elif pontuacao_maquina>pontuacao_usuario:
            print("VOCÊ PERDEU")
        else:
            print("EMPATE")
        break
    maquina=choice(lista)
    if maquina==escolha:
        print('Empate!')
    elif escolha=='R' and maquina=='T':
        print(f"Você ganhou!\nA máquina jogou {maquina}, e você {escolha}.")
        pontuacao_usuario+=1
    elif escolha=='T' and maquina=='P':
        print(f"Você ganhou!\nA máquina jogou {maquina}, e você {escolha}.")
        pontuacao_usuario+=1
    elif escolha=='P' and maquina=='R':
        print(f"Você ganhou!\nA máquina jogou {maquina}, e você {escolha}.")
        pontuacao_usuario+=1
    else:
        print(f"Você perdeu!\nA máquina jogou {maquina}, e você {escolha}.")
        pontuacao_maquina+=1

    

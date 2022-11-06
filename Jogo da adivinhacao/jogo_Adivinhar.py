from random import randint
print('='*50)
print('Jogo da Adivinhação'.center(50))
print('='*50)

while True:
    teto=input('Até que número você quer que sorteie? ').strip()
    while teto.isnumeric()==False:
        print('VALOR INCORRETO!!!')
        teto=input('Até que número você quer que sorteie? ').strip()
        if teto.isnumeric()==True:
            break
    teto=int(teto)
    sorteio=randint(0,teto)
    escolha_usuario=input('Adivinhe o número: ')
    while escolha_usuario.isnumeric()==False:
        print('VALOR INCORRETO!!!')
        escolha_usuario=input('Adivinhe o número: ').strip()
        if escolha_usuario.isnumeric()==True:
            break
    escolha_usuario=int(escolha_usuario)
    tentativas=1
    while escolha_usuario!=sorteio:
        if escolha_usuario>sorteio:
            print('O valor sorteado foi menor!')
            tentativas+=1
        elif sorteio>escolha_usuario:
            print('O valor escolhido é maior')
            tentativas+=1
        else:
            break
        escolha_usuario=int(input('Adivinhe o número: '))
    print(f"Você acertou!!\nO valor era {sorteio} e você acertou em {tentativas} tentativas")
    op=str(input('Deseja jogar novamente? [S/N]: ')).strip().upper()
    while op!='N' and op!='S':
        op=str(input('Valor incorreto!\nDeseja jogar novamente? [S/N]: ')).strip().upper()
    if op=='N':
        break
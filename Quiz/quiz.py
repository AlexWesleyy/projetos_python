from time import sleep
print("Seja muito bem vindo ao quiz Copa do Mundo!")
answer_user = input("Quer começar? (S/N) ").upper().strip()
while answer_user!="N" and answer_user!="S":
    answer_user = input("Valor incorreto! Quer começar? (S/N) ").upper().strip()
if answer_user=="N":
    quit()

if answer_user=="S":
    while True:
        score = 0
        print("Começando...")
        sleep(2)
        print("Quando foi a primeira edição da copa? \n (A) Em 1986 - Alemanha \n (B) Em 1930 - Uruguai \n (C) Em 1935 - México \n (D) Em 1950 - Brasil \n")
        answer_1 = input("Resposta: ").upper().strip()

        if answer_1 == "B":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        print("Onde o futebol foi criado?\n (A) Alemanha \n (B) Brasil \n (C) Inglaterra \n (D) Uruguai \n")
        answer_2 = input("Resposta: ").upper().strip()

        if answer_2 == "C":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        print(f"Quiz acabou... Pontuação: {score}/2")
        if score<2:
            op=str(input("Tentar Novamente? S/N ")).upper().strip()
            while op!="N" and op!="S":
                op = input("Valor incorreto! Quer tentar novamente? (S/N) ").upper().strip()
            if op=="N":
                break
            else:
                continue
        else:
            break
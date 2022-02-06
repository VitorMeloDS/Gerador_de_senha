import random

#Listas com as letras caracteres e numeros para gerar a senha
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

caracteres = ["!", "@", "#", "$", "&"]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Entrada com os numeros de digitos que a senha possue
tamanho = input("""
    \033[7:30:47m                    Gerador de senha                    \033[m
    \033[1:30:47m========================================================\033[m
    \033[1:30:47mTamanhos de senhas suportadas são com 4, 6 ou 8 digitos!\033[m
    \033[0:30:47m                                                        \033[m
    \033[4:30:47mDigite o tamanho da senha que deseja:\033[m""").strip()

#If para a senah de 4 digitos 
if tamanho == "4":
    contador = 0 
    senha = []
    while contador < 4:
        sorteio = random.choice(numeros)
        senha.append(sorteio)
        contador+=1
    print("""
    \033[7:30:47m      senha de 4 digitos!      \033[m
    \033[1:30:47m===============================\033[m
    \033[0:30:47m                               \033[m
    \033[1:30:42mOlá usuário a sua senha é: {}{}{}{}\033[m
    """.format(senha[0], senha[1], senha[2], senha[3]))

#Elif para a senha de 6 digitos 
elif tamanho == "6":
    contador = 0 
    senha = []
    while contador < 6:
        if contador < 3:
            sorteio = random.choice(letras)
            senha.append(sorteio)
            contador+=1

        if contador == 3 :
            sorteio = random.choice(caracteres)
            senha.append(sorteio)
            contador+=1

        if contador > 3:
            sorteio = random.choice(numeros)
            senha.append(sorteio)
            contador+=1
    print("""
    \033[7:30:47m       senha de 6 digitos!       \033[m
    \033[1:30:47m=================================\033[m
    \033[0:30:47m                                 \033[m
    \033[1:30:42mOlá usuário a sua senha é: {}{}{}{}{}{}\033[m
    """.format(senha[0], senha[1], senha[2], senha[3], senha[4], senha[5]))

#Elif para a senha de 8 digitos
elif tamanho == "8":
    contador = 0 
    senha = []
    while contador < 8:
        if contador <= 3:
            sorteio = random.choice(letras)
            senha.append(sorteio)
            contador+=1

        if contador == 4 or contador == 5:
            sorteio = random.choice(caracteres)
            senha.append(sorteio)
            contador+=1

        if contador > 5:
            sorteio = random.choice(numeros)
            senha.append(sorteio)
            contador+=1
    print("""
    \033[7:30:47m        senha de 8 digitos!        \033[m
    \033[1:30:47m==================================+\033[m
    \033[0:30:47m                                   \033[m
    \033[1:30:42mOlá usuário a sua senha é: {}{}{}{}{}{}{}{}\033[m
    """.format(senha[0], senha[1], senha[2], senha[3], senha[4], senha[5], senha[6], senha[7]))

#Else para caso o usuário digite algo em não esta no padrão dos digitos da senhas
else:
    print("""
    \033[7:31:40m                               AVISO!                                \033[m
    \033[1:31:40m=====================================================================\033[m
    \033[1:31:40mOps tem algo errado, verifique se digitou o tamanho da senha correto!\033[m
    \033[1:31:40m=====================================================================\033[m""")
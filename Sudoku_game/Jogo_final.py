import time

grelha_recebida = [0, 0, 0, 0, 0, 0, 0, 0, 0]
grelha1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
saved_time = 0
grelha_check = [
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True, True]]


def open_game():
    print("Quer jogar do inicio ou resumir ? (new/resume)")

    option = input()

    while (option.lower() != "new" and option.lower() != "resume"):
        print("Quer jogar do inicio ou resumir ? (new/resume)")
        option = input()

    if option.lower() == "new":

        ficheiro = open("Sudoku/Jogo.txt", "r")

        linha = ficheiro.readlines()
        for i in range(9):
            grelha_recebida[i] = linha[i].split(" ")
            grelha1[i] = linha[i].split(" ")

        start_time = 0

        ficheiro.close()

    if option.lower() == "resume":

        ficheiro = open("Sudoku/Jogo_salvo.txt", "r")
        ficheiro_1 = open("Sudoku/Jogo.txt", "r")

        linha = ficheiro.readlines()
        linha_1 = ficheiro_1.readlines()

        for i in range(19):
            if i < 9:
                grelha_recebida[i] = linha[i].split(" ")[0:9]
                grelha1[i] = linha_1[i].split(" ")

            if 8 < i < 18:
                grelha_check[i - 9] = linha[i].split(" ")[0:-1]

            else:
                start_time = linha[-1]

        ficheiro.close()
        ficheiro_1.close()

        for i in range(9):
            for j in range(9):
                if grelha_check[i][j] == 'True':
                    grelha_check[i][j] = True
                else:
                    grelha_check[i][j] = False

    for i in range(9):
        for j in range(9):
            grelha_recebida[i][j] = int(grelha_recebida[i][j])
            grelha1[i][j] = int(grelha1[i][j])
            if grelha_recebida[i][j] == 0:
                grelha_recebida[i][j] = " "
            if grelha1[i][j] == 0:
                grelha1[i][j] = " "

    return start_time, grelha_check


regras = "Regras: \n 1:Na escolha do jogo, selecione o número do jogo relativo ao documento de texto no qual sua grelha esta inserida. \n 2:Em 'Ação' utilize 'c' para continuar ou 'p' para pausar, salvar e fechar o jogo. \n 3:Todos os números de uma linha devem ser diferentes. \n 4:Todos os números de uma coluna devem ser diferentes. \n 5:Todos os números de cada respectivo quadrado devem ser diferentes. \n 6:O mesmo número deve estar em posições diferentes em cada quadrado 3x3. \n "


# print do tabuleiro de sudoku com alguns números preenchidos #
def tabuleiro(jogo, grelha1):
    test = 0
    azul = '\033[0;36m'
    end = '\033[0m'
    Extremos = "||=============================||"
    Meio = "||---------|---------|---------||"
    print(Extremos)
    for i in range(9):
        for j in range(9):
            if ((i == 3 or i == 6) and j == 0): #2 do meio
                test += 1
                print(Meio)
            if (j == 0):  #9 da lateral esquerda
                test += 1
                print("|| ", end=" ")
            if (j == 3 or j == 6):  #18 das linhas centrais
                test += 1
                print(" | ", end=" ")
            if grelha1[i][j] != " ":  #22 números ja disponiveis na grelha
                test += 1
                print(azul + str(jogo[i][j]) + end, end=" ")
            if grelha1[i][j] == " ":  #59 espaços para preencher
                test += 1
                print(jogo[i][j], end=" ")
            if (j == 8):  #9 da lateral direita
                test += 1
                print(" ||")
    print(Extremos)
    return test
    finalizar(jogo)

def finalizar(j):
    test = 0
    if any(" " in sublist for sublist in j):
        test += 1
        return test
        jogada(j)
    else:
        return test
        salvar()

def jogada(jogo_novo, grelha1, grelha_check):
    # permitir ao jogador realizar um jogada (inserir um número numa célula vazia através das suas cordenadas) #
    test = 0
    ação = str(input("Ação: "))

    while ação != "c" and ação != "p":
        ação = str(input("Ação: "))

    if ação.lower() == "c":


        i = int(input("Número da linha: ")) - 1
        j = int(input("Número da coluna: ")) - 1

        if 0 <= i < 9 and 0 <= j < 9:
            test += 1

            if grelha1[i][j] == " ":
                test += 1
                numero_novo = int(input("Número a inserir: "))

                if numero_novo > 9 or numero_novo < 1:
                    print("Jogada inválida! O número deve estar entre 1 e 9.")

            else:
                print("Não pode mudar o número desta posição.")
                jogada(jogo_novo)

        else:
            print("Número da linha e da coluna devem estar entre 1 e 9")

        return test
        check(jogo_novo, i, j, numero_novo)

    if ação.lower() == "p":
        f = open("Sudoku/Jogo_salvo.txt", "w")
        for linha in jogo_novo:
            for j in linha:
                if j == " ":
                    f.write(str(0) + " ")
                    test += 1
                else:
                    test += 1
                    f.write(str(j) + " ")
            f.write("\n")

        for linha in grelha_check:
            for j in linha:
                test += 1
                f.write(str(j) + " ")
            f.write("\n")
        #end = time.time()
        saved_time = 0
        start_time = 2
        end = 5
        final_time = int(saved_time) + (end - start_time)  # o tempo salvo do pause + o tempo a mais que estive a jogar
        if final_time == 3:
            test += 1
        f.write(f"{final_time:.0f}")
        print("O jogo foi salvo como 'Jogo_salvo.txt'")
        f.close()
        return test


def check(jogo_, i, j, numero_novo):
    test = 0
    erros = [True, True, True, True]
    linha = jogo_[i]
    coluna = []
    for x in jogo_:
        coluna.append(x[j])

    if numero_novo in linha and jogo_[i][j] != numero_novo:
        test += 1
        erros[0] = False
    if numero_novo not in jogo_[i]:
        erros[0] = True

    if numero_novo in coluna and jogo_[i][j] != numero_novo:
        test += 1
        erros[1] = False
    if numero_novo not in coluna:
        erros[1] = True

    quadrado = []
    quadrado_i = (i // 3) * 3
    quadrado_j = (j // 3) * 3
    for x in range(3):
        for y in range(3):
            quadrado.append(jogo_[quadrado_i + x][quadrado_j + y])
    if numero_novo in quadrado and jogo_[i][j] != numero_novo:
        test += 1
        erros[2] = False
    if numero_novo not in quadrado:
        erros[2] = True

    posição = []
    a = 0
    b = 0
    _i = (i // 3)
    _j = (j // 3)
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            if i == 3 or i == 7:
                a = (_i - 1)
            if i == 5:
                a = (_i + 1)
            if i == 6:
                a = (_i - 2)
            if i <= 2:
                a = i
            if i == 4 or i == 8:
                a = _i
            if j == 3 or j == 7:
                b = (_j - 1)
            if j == 5:
                b = (_j + 1)
            if j == 6:
                b = (_j - 2)
            if j <= 2:
                b = j
            if j == 4 or j == 8:
                b = _j
            posição.append(jogo_[a + y][b + x])
    if numero_novo in posição and jogo_[i][j] != numero_novo:
        test += 1
        erros[3] = False
    if numero_novo not in posição:
        erros[3] = True

    if False in erros:
        grelha_check[i][j] = False

    jogo_[i][j] = numero_novo

    if any(" " in sublist for sublist in jogo_):
        return test
        tabuleiro(jogo_)

    else:
        erro_1 = False

        for i in range(9):
            for j in range(9):
                if grelha_check[i][j] == False:
                    jogo_[i][j] = '\033[1;31m' + str(jogo_[i][j]) + '\033[0m'
                    erro_1 = True

        if erro_1:
            print("Número(os) na mesma linha.")
            print("Número(os) na mesma coluna.")
            print("Número(os) no mesmo quadrado.")
            print("Número(os) na mesma posição em outro quadrado.")

        return test
        tabuleiro(jogo_)


def salvar(saved_time, end, start_time):
    f = open("Sudoku/Jogo_Timer.txt", "a")
    #end = time.time()
    final_time = int(saved_time) + (end - start_time)
    f.write(f"Tempo final: {final_time:.0f} segundos \n")
    print("Terminado!")
    print(f"Tempo final: {final_time:.0f} segundos \n")
    f.close()
    return final_time

if __name__ == '__main__':
    print(regras)
    saved_time, grelha_check = open_game()
    start_time = time.time()
    tabuleiro(grelha_recebida)
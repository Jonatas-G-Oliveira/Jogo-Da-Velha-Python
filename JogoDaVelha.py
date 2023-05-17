def geraTabuleiro():
    t = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(3):
        for j in range(3):
           t[x][j] = '.'
    return t


def imprimeTabuleiro(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            print(tabuleiro[linha][coluna],end = ' ')
        print()


def jogar(tabuleiro,jogador,linha,coluna):
    if tabuleiro[linha-1][coluna-1] == '.':
        if jogador == 0:
            tabuleiro[linha-1][coluna-1] = 'X'
            return tabuleiro,True
        if jogador == 1:
            tabuleiro[linha-1][coluna-1] = 'O'
            return tabuleiro,True
    else:
        print(f'\n    Linha {linha} e coluna {coluna} já utilizada\n')
        return tabuleiro,False


def verificar(tabuleiro,jogador):
    if jogador == 0:
        for casos in range(0, 5):
            s = 0
            if casos == 0:                      #Diagonal Principal
                for l in range(len(tabuleiro)):
                    for c in range(len(tabuleiro)):
                        if l == c:
                            if tabuleiro[l][c] == 'X':
                                s += 1
                            if s == 3:
                                print('O 1º JOGADOR [X] VENCEU!!!')
                                return True
            if casos == 1:                      #Linhas
                for l in range(len(tabuleiro)):
                    s = 0
                    for c in range(len(tabuleiro)):
                        if tabuleiro[l][c] == 'X':
                            s += 1
                        if s == 3:
                            print('O 1º JOGADOR [X] VENCEU!!!')
                            return True
            if casos == 2:                      #Colunas
                for l in range(len(tabuleiro)):
                    s = 0
                    for c in range(len(tabuleiro)):
                        if tabuleiro[c][l] == 'X':
                            s += 1
                        if s == 3:
                            print('O 1º JOGADOR [X] VENCEU!!!')
                            return True
            if casos == 3:
                linha = 0                             #Diagonal Secundaria
                coluna = len(tabuleiro)-1
                for x in range(len(tabuleiro)):
                    if tabuleiro[linha][coluna] == 'X':
                        s += 1
                    if s == 3:
                        print('O 1º JOGADOR [X] VENCEU!!!')
                        return True
                    linha += 1
                    coluna -= 1
            if casos == 4:
                s = 0
                for l in range(len(tabuleiro)):
                    for c in range(len(tabuleiro)):
                        if tabuleiro[l][c] == '.':
                            s += 1
                if s == 0:
                    print('DEU VELHA')
                    return True

    if jogador == 1:
        for casos in range(0,5):
            s = 0
            if casos == 0:  # Diagonal Principal
                for l in range(len(tabuleiro)):
                    for c in range(len(tabuleiro)):
                        if l == c:
                            if tabuleiro[l][c] == 'O':
                                s += 1
                            if s == 3:
                                print('O 2º JOGADOR [O] VENCEU!!!')
                                return True
            if casos == 1:                      #Linhas
                for l in range(len(tabuleiro)):
                    s = 0
                    for c in range(len(tabuleiro)):
                        if tabuleiro[l][c] == 'O':
                            s += 1
                        if s == 3:
                            print('O 2º JOGADOR [O] VENCEU!!!')
                            return True
            if casos == 2:                      #Colunas
                for l in range(len(tabuleiro)):
                    s = 0
                    for c in range(len(tabuleiro)):
                        if tabuleiro[c][l] == 'O':
                            s += 1
                        if s == 3:
                            print('O 2º JOGADOR [O] VENCEU!!!')
                            return True
            if casos == 3:
                linha = 0                             #Diagonal Secundaria
                coluna = len(tabuleiro)-1
                for x in range(len(tabuleiro)):
                    if tabuleiro[linha][coluna] == 'O':
                        s += 1
                    if s == 3:
                        print('O 2º JOGADOR [O] VENCEU!!!')
                        return True
                    linha += 1
                    coluna -= 1
            if casos == 4:                      #Velha
                s = 0
                for l in range(len(tabuleiro)):
                    for c in range(len(tabuleiro)):
                        if tabuleiro[l][c] == '.':
                            s += 1
                if s == 0:
                    print('DEU VELHA')
                    return True


def main():
    tabuleiro = geraTabuleiro()
    imprimeTabuleiro(tabuleiro)
    jogadas = 1
    jogador = 0
    while True:
        if jogador == 0:                                           
            while True:
                print(f'Jogador {jogador+1}:Jogada{jogadas}')
                linha = int(input('Qual linha você quer marcar? '))
                coluna = int(input('Qual coluna você quer marcar '))
                t,repetido = jogar(tabuleiro,jogador,linha,coluna)
                imprimeTabuleiro(t)
                if repetido == True:
                    jogadas += 1 
                    break
            if jogadas >= 6:
                fim = verificar(t,jogador)
                if fim == True:
                    break
            jogador = 1

        if jogador == 1:
            while True:
                print(f'Jogador {jogador+1}:Jogada{jogadas}')
                linha = int(input('Qual linha você quer marcar? '))
                coluna = int(input('Qual coluna você quer marcar '))
                t,repetido = jogar(tabuleiro,jogador,linha,coluna)
                imprimeTabuleiro(t)
                if repetido == True:
                    jogadas += 1
                    break
            if jogadas >= 6:
                fim = verificar(t,jogador)
                if fim == True:
                    break
            jogador = 0       
    print('Fim')                    

main()

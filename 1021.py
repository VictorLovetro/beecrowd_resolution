nota = float(input())
lista_dinheiro = [100,50,20,10,5,2]
lista_moeda = [1,0.50,0.25,0.10,0.05,0.01]
dinheiro = 0
moeda = 0


for n in lista_dinheiro:

    if n == 100:
        cem = nota // 100
        dinheiro = nota % 100

    elif n == 50:
        cinquenta = dinheiro // 50
        dinheiro = dinheiro  % 50
    
    elif n == 20:
        vinte = dinheiro // 20
        dinheiro = dinheiro %20
    
    elif n == 10:
        dez = dinheiro // 10
        dinheiro = dinheiro % 10 
    
    elif n == 5:
        cinco = dinheiro // 5
        dinheiro = dinheiro % 5

    elif n == 2:
        dois = dinheiro // 2
        dinheiro = dinheiro % 2

    for m in lista_moeda:
        if m == 1:
            um = dinheiro // 1
            moeda = dinheiro % 1

        elif m == 0.50:
            ciquenta_centavos = moeda // 0.50
            moeda = dinheiro % 0.50

        elif m == 0.25:
            vinte_cinco_centavos = moeda // 0.25
            moeda = dinheiro % 0.25

        elif m == 0.10:
            dez_centavos = moeda // 0.10
            moeda = dinheiro % 0.10

        elif m == 0.05:
            cinco_centavos = moeda // 0.05
            moeda = dinheiro % 0.05

        elif m == 0.01:
            um_centavo = moeda // 0.01
            moeda = dinheiro % 0.01
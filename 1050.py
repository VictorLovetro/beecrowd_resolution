ddd = int(input())

ddd_dict = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

cidade = ddd_dict.get(ddd, "DDD nao cadastrado")
print(cidade)
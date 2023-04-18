def primo():
    qtd_total = 100
    primos = [1,2]
    cand_primo = 3
    qtd_encontrada = 2
    primo = 1

    while qtd_encontrada < qtd_total:
        for i in range(2, cand_primo):
            if cand_primo % i == 0:
                primo = 0
                break

        if primo == 1:
            primos.append(cand_primo)
            qtd_encontrada += 1

            if qtd_encontrada % 10 == 0:
                primos += "<br>"
        primo = 1
        cand_primo += 2


    return primos


print(primo())
def roots(a1, a2, a3, b1, b2, b3):

    #Echte Koeffizienten, Elemente der Liste

    c_0 = a3*b3
    c_1 = a2*b3 + a3*b2
    c_2 = a1*b3 + a2*b2 + a3*b1
    c_3 = a1*b2 + a2*b1
    c_4 = a1*b1
    c_5 = 1

    koeffizientenliste = [c_5, c_4, c_3, c_2, c_1, c_0]

    #0 zählt nicht in VZW hinein

    koeffizientenliste_ohne_0 = [c for c in koeffizientenliste if c !=0]

    #Vorzeichenwechsel feststellen

    vzw = 0
    vorzeichen = 0  #0 für positiv, 1 für negativ

    for c in koeffizientenliste_ohne_0:
        if c < 0:
            neues_vorzeichen = 1
        else:
            neues_vorzeichen = 0

        if neues_vorzeichen != vorzeichen:
            vzw += 1
            vorzeichen = neues_vorzeichen

    #Rest ist trivial
    if vzw % 2 == 0:
        return 'Das Polynom hat eine gerade Anzahl von positiven reellen Nullstellen.'
    else:
        return 'Das Polynom hat eine ungerade Anzahl von positiven reellen Nullstellen.'

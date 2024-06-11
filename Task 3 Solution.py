def sieve(n):                           #Versuch 2 möglicherweise effizienteres Sieb, was nicht immer Listen durchgeht und Elemente entfernt
    primes = []
    is_prime = [True] * (n + 1)

    if n < 2:
        return "None"

    is_prime[0] = is_prime[1] = False  #0 und 1 sind keine Primzahlen

    for candidate in range(2, int(n**0.5) + 1):
        if is_prime[candidate]:
            primes.append(candidate)
            for Vielfaches in range(candidate * candidate, n + 1, candidate):
                is_prime[Vielfaches] = False

    for candidate in range(int(n**0.5) + 1, n + 1):
        if is_prime[candidate]:
            primes.append(candidate)

    return primes


def isprime(n):
    if n < 2:                               #trivial
        return "None"
    for i in range(2, int(n**0.5) + 1):     #es reicht alle Teiler kleiner als der Wurzel von n zu finden, da Zahlen darüber n nicht teilen werden int() rundet reelle wurzel ab
        if n % i == 0:                      #teilt i n, kann n keine Primzahl sein lol
            return False
    return True


def factorization(n):
    if n < 2:
        return "None"

    m = int(n**0.5)+1                              #Rechenaufwandsminimierung durch begrenzung von m durch wurzel m gerundet nach oben

    candidates = sieve(m)                       #Primfaktoren im Vorhinen Aussieben also ist candidates eine Liste mit candidate in candidates

    factors = []

    for candidate in candidates:
        exponent = 0
        while n % candidate == 0:                #Hier findet quasi Primfaktorzerlegung statt, nur dass gezählt wird wie oft a*a*a... in n passt und exponent für jedes a +1 geht
            n //= candidate                       #Kandidat wird dividiert also N= n/Kandidat
            exponent += 1                        #Exponent funktioniert hier als Zähler
        if exponent > 0:
            factors.append([candidate, exponent]) #wenn es exponent gibt ist p primfaktor und Liste factors wird mit liste aus cand und exp befüllt

    if n > 1:
        factors.append([int(n), 1])               #Wenn nach alledem n nicht reduziert wurde auf 1 muss n primsein also sich und 1 enthalten

    return factors


def euler_phi(n):

    factors = factorization(n)
    if n < 1:
        return "None"
    if n == 1:
        return 1

    if isprime(n) == True:
        return n - 1                                         #Eigenschaft der eulerschen Phi Funktion spart Laufzeit bzw rechenzeit phi(p) = p-1 für p = Primzahl


    result = 1
    for factor in factors:                      #Versuch 2 Laufzeitoptimierung
        prim, exp = factor
        result *= prim - 1
        result *= prim ** (exp-1)

    return result

def get_prime_factors_list(basis):                                 #Erstellt Liste aus Listeneinträgen der Faktoren z.b bei 24 gibt es uns [2, 3] , da 2^3*3^1 = 24 also nur die basen bzw Teiler
                                                                    # Hilfsfunktion, um die Liste der Primfaktoren zu erhalten als gesonderte Liste [0] da an erster stelle
    factors = factorization(basis)
    return [factor[0] for factor in factors]

def iscoprime(m, n):                                                #Versuche set für laufzeiteffizienz statt list
    if m < 1 or n < 1:
        return "None"

    # Optimierung: Wenn m oder n gleich 1 sind, sind sie immer teilerfremd
    if m == 1 or n == 1:
        return True

    # Berechne die Primfaktoren nur einmal für beide Zahlen
    factors_m = set(get_prime_factors_list(m))
    factors_n = set(get_prime_factors_list(n))

    # Überprüfe, ob es gemeinsame Primfaktoren gibt
    return not any(factor in factors_m for factor in factors_n)
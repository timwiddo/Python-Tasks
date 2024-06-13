def multiply(A,B):
    A = A.split(', ') #Matrix wird in Liste gepackt also die reihen
    B = B.split(', ')

    A = [list(map(int, row.split())) for row in A] #jede Reihe in Liste wird elementweise zu int und in neue Liste gepackt
    B = [list(map(int, row.split())) for row in B]

    m, r = len(A), len(A[0]) #klassisch lenA = Zeile lenA[0] = Spalte
    r, n = len(B), len(B[0])
    C = [['0' for _ in range(n)] for _ in range(m)] #Ergebnismatrix mit mxr*rxn = mxn

    for i in range(m):
        for j in range(n):
            min_val = float('inf') # um zu garantieren, dass erster gefunder Wert in minplus-Alg. auch entsprechend übernommen wird
            for k in range(r):
                min_val = min(min_val, A[i][k] + B[k][j]) #einfach nur mathemathematisches durchführen der Berechnung
            C[i][j] = str(min_val) #gef. Wert wird direkt wieder als String abgespeichert

    C_str = ', '.join([' '.join(row) for row in C])#Zeichenkette in gewünschte Form bringen [6, 8, 4] in '6 8 4' bspw für eine row

    return C_str


def power(A, m):

    result = A  # Kopie von A, um A für die Potenzierung nicht zu verändern

    for _ in range(m - 1):  # Bei der 2. Potenz wird A einmal mit sich selbst multipliziert, daher das
        result = multiply(result, A)  # Minplus Alg. in der Ergebnismatrix wird so berücksichtigt

    return result

def LU_decomposition(A_str):
    # Konvertiere den Eingabe-String in eine Matrix A
    A = [list(map(int, row.split())) for row in A_str.split(', ')] #String wie letzte Woche wird vorest in eine int Liste gepackt

    n = len(A)
    L = [[0] * n for _ in range(n)] #Leere Matrizen L,U werden erstellt (Listen aus Listen wie letzte woche)
    U = [[0] * n for _ in range(n)]

    for i in range(n): #L wird zur Einheitsmatrix gemäß vorgehen
        L[i][i] = 1

    for k in range(n):              #Hier wird der LU Algorithmus einfach nur angewendet in Codeform->Itererien Durch liste bzw zeilen
        for j in range(k, n):       #hier durch n-1 zeilen,in der Summe wird Zeile L mal Spalte U bis zur k-ten Stelle
            U[k][j] = A[k][j] - sum(L[k][p] * U[p][j] for p in range(k)) #L ist Einheitsm. mal U  Spalte und das summiert von A abgezogen)
            #print(U)
            #U[0][0] = A[0][0] -... und immer so weiter bis matrix U diagonalgestalt hat
        for i in range(k+1, n): #k+1 sorgt dafür dass wir immer unterhalb der Hauptdiagonalen sind
            L[i][k] = (A[i][k] - sum(L[i][p] * U[p][k] for p in range(k))) // U[k][k] #selbiges für L(untere Dreiecksmatrix)
            #print(L)

    #print(U)
    #print(L)




    R = [[U[i][j] if i <= j else L[i][j] for j in range(n)] for i in range(n)] #Übernimmt U elemente überhalb der Hauptdiagonalen und L unterhalb


    #ErgebnisMatrix R als String
    result_str = ', '.join([' '.join(map(str, row)) for row in R]) #von innen nach außen 1: Trennung durch ' '(Leerzeichen) dann
                                                                   # 2. Trennung durch komma der einzelnen Zeichenketten(rows)

    return result_str #bis hierhin stimmt alles, prüfe zweite funktion


def generate_LU_from_R(R):#empfängt string
    R = [list(map(int, row.split())) for row in R.split(', ')]#R in int list bzw Matrix
    n = len(R)
    L = [[0] * n for _ in range(n)]
    U = [row[:] for row in R]

    for i in range(n):
        L[i][i] = 1
        for j in range(i):
            L[i][j] = R[i][j] #kopiere notwendige Elemente aus R für L
            U[i][j] = 0  # Setze Elemente unterhalb der Hauptdiagonale auf 0

    return L, U # gibt zwei Listen LU bzw Matrizen zurück
def solve_LGS(A_str,B_str):

   A_nochStr = LU_decomposition(A_str) #LU gibt string zurück

   L, U = generate_LU_from_R(A_nochStr)# L U aus R extrahieren sozusagen

   A = [list(map(int, row.split())) for row in A_nochStr.split(', ')] #Str sind jetz listen
   B = [list(map(int, row.split())) for row in B_str.split(', ')]

   n = len(A)
   #Matrix zur Speicherung der Lösung
   X = [[0] * len(B[0]) for _ in range(n)] # hier wird matrix erstellt die mxn * nxz = mxz erfüllt

   #Löse LGS für jede Spalte in B
   for col in range(len(B[0])):
       #Konvertiere die Spalte von B in eine Liste
       b = [B[i][col] for i in range(n)] #b spalten als liste

       #Vorwärtssubstitution: L * Y = B
       Y = [0] * n #gemäß matrizenmultiplikationsgesetz
       for i in range(n):
           summation = sum(L[i][k] * Y[k] for k in range(i))#einfacher 1*y1 + 8*y2 +... als beispiel diese summe ist gemeint
           Y[i] = b[i] - summation #GL werden Zeilenweise gelöst lösungsvektor y wie in HA

       #Rückwärtssubstitution: U * X = Y
       X_column = [0] * n
       for i in range(n - 1, -1, -1): #Wir fangen unten in der Dreiecksmatrix an da sie in ZSF ist
           summation = sum(U[i][k] * X_column[k] for k in range(i + 1, n)) # bspw 4*x_3 = 4 #i +1 da uns alles unterhalb der diag nicht interessiert, da Nullen
           X_column[i] = (Y[i] - summation) / U[i][i]                       # hier teilen wir dann durch 4-> x_3 = 1 als bsp teile immer durch HDG, da das in jeweiliger Zeile gesucht is


       for i in range(n):
           X[i][col] = int(X_column[i]) #evtl Rundungsfehler mal sehen sollte eig nich -> LSGVektor X wie in HA

   #richtiges Ausgabeformat
   result_str = ', '.join([' '.join(map(str, row)) for row in X])

   return result_str









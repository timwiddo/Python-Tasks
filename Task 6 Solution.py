def find_first_larger(L, e):

    links, rechts = 0, len(L) - 1       # Wert ganz links und ganz rechts werden betrachtet bzw zugewiesen
    result = len(L)                     # Falls kein element gefunden wird soll ja laut aufg länge der liste ausgegeben werden

    while links <= rechts:
        mitte = (links + rechts) // 2   # brauchen wir für unsere log n laufzeit indem wir gleich liste splitten nach erstem durchlauf wieder gesplittet usw undsofort(Binäre Suche)


        if L[mitte] > e:              # Da L sortiert, können wir uns jetzt die eine bzw die andere hälfte der Liste angucken
                                        # je nachdem ob unser mittelwert schon größer oder kleiner als gegebenes e ist
                                        #HIER WIRD LINKE HÄLFTE DURCHSUCHT
            result = mitte              # Mitte wird jetzt wie ein Zeiger verwendet der durch die Hälfte durchwandert da rechts minimiert wird
            rechts = mitte - 1          # Mitte wird verschoben und rechts ist neues ende(da alles gr. oder kleiner e irrelevant is) um e näher zu kommen sozusagen
        else:
                                        #Hier selbes Prinzip nur mit rechter hälfte
            links = mitte + 1

    return result

def binary_search_next_unique(L, start): #Hilfsfunktion um k log n zu gewährleisten


     # L: Eine aufsteigend sortierte Liste
     # start: Der Startindex für die Suche
     # return: Der Index des nächsten einzigartigen Elements

    links, rechts = start, len(L) - 1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if L[mitte] == L[start]:
            links = mitte + 1
        else:
            rechts = mitte - 1

    return links if links < len(L) else None #wenn links noch in L liegt gib es zurück andernfalls wars das mit der suche

def unique(L):

    if not L:
        return [] #trivialfall

    result = []     #ergebnisliste
    i = 0          #Zählvariable bzw indexvariable

    while i < len(L):
        result.append(L[i])
        next_index = binary_search_next_unique(L, i) # BS wird k mal ausgeführt da es immer alle n doppelten aussortiert
        if next_index is None:
            break # hört auf wenn binary nichts mehr findet dann sind wir fertig
        i = next_index # i übernimmt nun position seines nachfolgers

    return result


"""
L = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 6]
result1 = find_first_larger(L, 2)
result2 = unique(L)
print(result1)
print(result2)
"""

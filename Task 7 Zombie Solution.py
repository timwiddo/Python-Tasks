import random


def updatePosition(n, m, pos, rnd):
    # Berechnet die aktuelle Zeile und Spalte aus der Position
    Zeile = pos // m  #im 3x5 viereck wenn element auf der 7 steht ist 7//5=1 also 2te zeile weil wir bei 0 starten
    Spalte = pos % m   #hier ist 7%5=2 also 2te zeile 3te Position

    # Bestimmt die Bewegungsrichtung basierend auf rnd
    if 0 <= rnd < 0.25:
        # Bewegung nach rechts
        Spalte = (Spalte + 1) % m   # mod m sorgt für den Bernd das Brot Effekt -> rechts raus links rein
    elif 0.25 <= rnd < 0.5:
        # Bewegung nach links
        Spalte = (Spalte - 1) % m
    elif 0.5 <= rnd < 0.75:
        # Bewegung nach unten
        Zeile = (Zeile + 1) % n
    elif 0.75 <= rnd < 1:
        # Bewegung nach oben
        Zeile = (Zeile - 1) % n

    # Berechnet die neue Position aus der Zeile und Spalte
    new_pos = Zeile * m + Spalte
    return new_pos
"""Zum Beispiel, wenn eine Figur sich in der dritten Zeile (Zeilenindex 2) und der zweiten 
Spalte (Spaltenindex 1) eines 5-Spalten-Vierecks befindet, wäre die eindimensionale Position 2 * 5 + 1 = 11"""

#Testen der Funktion mit den gegebenen Beispielen
"""test1 = updatePosition(3, 5, 0, 0.3)  # Erwarteter Output: 4
test2 = updatePosition(3, 5, 4, 0.8) # Erwarteter Output: 14
print(test1, test2)"""

def updatePositions(n, m, positions):
    # Update für alle Elemente des Vierecks bzw der Liste
    for i in range(len(positions)):
        # Zufallszahl für rnd
        rnd = random.random()
        # Aktualisiere Position
        fig, pos = positions[i] #neuer Versuch vorher gabs problem mit übergabe
        new_pos = updatePosition(n, m, pos, rnd)
        positions[i] = [fig, new_pos]

def sortPositions(positions):
    # Sortiere die Liste nach dem zweiten Eintrag jeder Teilliste
    # mithilfe von Lambda(funktion) können wir das hier einfacher definieren
    positions.sort(key=lambda pos: pos[1]) # sortiert also unsere Liste anhand der elemente an index 1 (2ter Stelle) das definiert lambda
"""positions = [['Z', 184], ['Z', 161], ['Z', 160], ['Z', 160]]
sortPositions(positions)
print(positions)"""

def extractSquare(positions):
    # Sortiere positions nach dem zweiten Eintrag jeder Teilliste(siehe Funktion darüber)
    sortPositions(positions)

    # Finde den höchsten Index
    highest_index = positions[-1][1] # wir gehen an letztes element mit [-1] und an 2te stelle mit [1]

    # Extrahiere alle Figuren mit diesem Index
    square = [p for p in positions if p[1] == highest_index] #alle el aus positions die den höchsten index haben werden in neue square liste gepackt

    # Entferne diese Figuren aus positions
    positions = [p for p in positions if p[1] != highest_index]# alle el aus pos die nicht highindex haben bleiben in pos

    return positions, square



"""positions = [['Z', 160], ['Z', 160], ['Z', 161]]
positions, square = extractSquare(positions)
print(positions)
print(square)"""

def giftExchange(square):
    # Zähle die verschiedenen Typen von Figuren auf dem Index-Feld: _ bedeutet posi ist irrelevant aber existent(Platzhalter)
    count_z = sum(1 for fig, _ in square if fig == 'Z')
    count_zh = sum(1 for fig, _ in square if fig == 'ZH')
    count_h = sum(1 for fig, _ in square if fig == 'H')
    count_hh = sum(1 for fig, _ in square if fig == 'HH')

    # a)
    if count_zh >= 1 and count_h >= 1 : # Anweisung in der HA
        square[:] = [[('HH' if fig == 'H' else fig), pos] for fig, pos in square] # menschen werden zu harfenmenschen andernfalls passiert nüscht
        # Aktualisierung der Zählungen nach a)                                     #[:] bewirkt, dass die änderungen nicht in lokaler kopie sondern in square selst gemacht werden!
        count_hh = sum(1 for fig, _ in square if fig == 'HH')
        "print(count_hh)"
          # musste jetz hier die liste Sortieren lassen da mein output ZH, HH war statt HH, ZH

    # b)
    if count_z >= 1 and (count_h >= 1 or count_hh >= 1): # Anweisung in der HA
        if count_z >= 2 * count_hh:
            # Alle Menschen (mit oder ohne Harfe) in Zombies umwandeln
            square[:] = [['Z', pos] if fig in ['H', 'HH'] else [fig, pos] for fig, pos in square]

        elif count_z < 2 * count_hh :
            # Alle Zombies in Elfen-Zombies umwandeln
            square[:] = [['ZH', pos] if fig == 'Z' else [fig, pos] for fig, pos in square]

    square.sort(key=lambda typ: typ[0])  # musste jetz hier die liste Sortieren lassen da mein output ZH, HH war statt HH, ZH

    "return square"


"""square = [['ZH', 238], ['H', 238]]
giftExchange(square)
print(square)"""
"""square = [['H', 160], ['H', 160], ['Z', 160], ['ZH', 160]]
print(giftExchange(square))"""

def mergeSquare(square, intermediate):
    # Füge alle Elemente von square zu intermediate hinzu
    intermediate.extend(square)
    return intermediate

"""intermediate = [['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]
intermediate = mergeSquare([['Z', 159], ['Z', 159]],intermediate)
print(intermediate)"""

def christmasFated(positions):
    # Zähle die verschiedenen Typen von Figuren
    count_z = sum(1 for fig, _ in positions if fig == 'Z')
    count_zh = sum(1 for fig, _ in positions if fig == 'ZH')
    count_other = sum(1 for fig, _ in positions if fig not in ['Z', 'ZH'])

    # Überprüfe die Bedingungen
    if count_other == 0: # nur noch Z oder ZH
        return True
    elif count_z == 0 and count_other >= 1: # keine zombies Z nur H oder HH
        return True
    else:
        return False
"""print(christmasFated([['HH', 80], ['HH', 98], ['Z', 4], ['HH', 64], ['Z', 76]]))

print(christmasFated([['HH', 160], ['Z', 160], ['ZH', 160]]))"""

def christmasFate(positions):
    count_z = sum(1 for fig, _ in positions if fig == 'Z')
    count_zh = sum(1 for fig, _ in positions if fig == 'ZH')
    count_other = sum(1 for fig, _ in positions if fig not in ['Z', 'ZH'])
    count_h = sum(1 for fig, _ in positions if fig == 'H')
    count_hh = sum(1 for fig, _ in positions if fig == 'HH')

    # Überprüfe die Bedingungen
    if (count_z > 0 or count_zh > 0) and count_other == 0: #Z und ZH only
        return 'Zombies ate my Christmas!'
    elif count_z == 0 and (count_h > 0 or count_hh > 0): # keine z aber dafür gibts mind 1 mensch h oder hh
        return 'Ho, ho, ho, and a merry Zombie-Christmas!'

"""print(christmasFate([['HH', 160], ['HH', 160], ['ZH', 160], ['ZH', 160]]))

print(christmasFate([['Z', 160], ['Z', 160], ['ZH', 160], ['ZH', 160]]))"""

def zombieChristmas(n, m, positions):
    # Hält Zwischenstände der Positionen
    aktuelle_positions = positions.copy()  # Korrekte Erstellung der Kopie

    # Simulation beginnt
    while not christmasFated(aktuelle_positions):
        # Aktualisiere Positionen
        updatePositions(n, m, aktuelle_positions)

        updated_positions = []

        while aktuelle_positions:
            #  Figuren auf dem gleichen Feld extracten
            aktuelle_positions, square = extractSquare(aktuelle_positions)

            # Führe tausch auf Feld durch
            giftExchange(square)

            # Füge das aktualisierte "Quadrat" zu den aktualisierten Positionen hinzu
            updated_positions = mergeSquare(square, updated_positions)

        # Aktualisiere aktuelle_positions für den nächsten Schritt
        aktuelle_positions = updated_positions

    # Gib das Schicksal von Weihnachten aus
    fate = christmasFate(aktuelle_positions)
    print(fate)

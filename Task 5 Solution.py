from collections import deque                           # BFS ranholen
                                                        # die gelben ausrufezeichen gehen nicht weg



def abstand(s,t,dateiname="labyrinth.dat"):


                                                        # Funktion für das Einlesen des Labyrinths aus der Datei
    def read_labyrinth(dateiname):                       # Hilfsfunktion um labyrinth gut einzulesen
        laby = []
        with open(dateiname, 'r') as file:
            for line in file:                               # labyrinth wird nun angefügt zeile für zeile
                laby.append(list(line.strip()))             # .strip entfernt überflüssige Leerzeichen
                                                            # [['U', 'P', 'P', 'P', 'U', 'P', 'P', 'P', 'U', 'P'], <- so sieht laby jetzt aus!! also nachdem forloop zu ende is
                                                            #  ['P', 'U', 'U', 'P', 'P', 'P', 'U', 'U', 'U', 'P'],<-bzw so sieht es aus für das File labyrinth.dat
                                                            # ['P', 'P', 'P', 'U', 'U', 'U', 'P', 'P', 'P', 'P'],
                                                            # ['U', 'U', 'P', 'P', 'P', 'P', 'P', 'U', 'U', 'P']]
        return laby




    # Funktion für die Bfs
    def bfs(starting_point, target_point, laby):
        if starting_point == target_point:                     # trivialer fall start=ziel
            return int(0)                       # erzeugt aus irgendeinem Grund TypeError?????
        rows, columns = len(laby), len(laby[0]) # len(laby) hier 4 sieht man gut an laby liste oben wie das mit zeilen und spalten hinhaut
        visited = set()                         # Set von besuchten Ps is hier laufzeitmäßig entspannter
        consecutive_steps = 0
        queue = deque([(starting_point, 0, consecutive_steps)])          # (Position, Schritte, Schritte in dieselbe Richtung)

        while queue:                            # BFS legt los
            (current, steps, consecutive_steps) = queue.popleft()       # current=aktuelle Posi,steps=zählt Schritte, cons steps= max 4 sein


            if current not in visited:                                  # bedeutet quasi wir gehen currents durch und tun sie dann in visited rein->siehe Mathematische HA Blatt6
                visited.add(current)
                i, j = current                                          # i, j logischerweise die "Koordinaten"(x, y)

                #Nachbarn hinzufügen
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]    # Nachbarn von P links rechts "oben unten"
                nice_neighbors = [(x, y) for x, y in neighbors if 0 <= x < rows and 0 <= y < columns and 0 <= x < len(laby) and 0 <= y < len(laby[0]) and laby[x][y] == 'P']

                                                                                # x muss zwischen 0 und rows sein logisch, y zwischen 0 und spalten
                                                                                # in neighbors, da nur nachbarn die nice sind relevant sind also im gültigen bereich und natürlich P für passierbar
                for neighbor in nice_neighbors:
                    if current == target_point: #evtl war das hier der gamechanger mal schaun
                        return steps
                        #Überprüfung auf dieselbe Richtung
                    if neighbor[0] == current[0] and neighbor[1] == current[1]:                                    # wenn der nice nachbar in dieselbe Richtung "zeigt"
                        queue.append((neighbor, steps + 1, consecutive_steps))# <- dat ding kommt jetz in die Queue

                    else:                                                       # IRGENDWO HIER STIMMT WAS NICH!!!!!!!!!!!!!
                        queue.append((neighbor, steps + 1, 1))                      # Richtungsänderung


        else:  # trivial: Wenn keine Verbindung gefunden wurde
            return -1

    #Labyrinth aus der Datei lesen
    laby = read_labyrinth(dateiname) #labys vorher labyrinth

    #Start und Zielpunkt für die Bfs also das was uns gegeben wird vom comajudge
    starting_point = (s[0], s[1])
    target_point = (t[0], t[1])

    #bfs aufrufen für genau diese punkte
    result = bfs(starting_point, target_point, laby)
    return result


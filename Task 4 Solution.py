def get_linedistance(points, line):

    m, b = line
    total_distance = 0

    for point in points:
        x, y = point
        #Berechne den y-Wert auf dem Graphen für die gegebenen x-Koordinaten
        y_on_graph = m * x + b
        #Berechne den quadratischen Abstand und summiere ihn auf
        distance = (y - y_on_graph) ** 2
        total_distance += distance

    #Gibt den quadratischen Gesamtabstand zurück
    return total_distance

def get_optimal_line(points):
    #Berechne die Anzahl der Punkte
    n = len(points)

    #Berechne die Summen der x- und y-Werte
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)

    #Berechne die Mittelwerte der x- und y-Werte
    middle_x = sum_x / n
    middle_y = sum_y / n

    #Berechne die Steigung a und den y-Achsenabschnitt b
    numerator = sum((point[0] - middle_x) * (point[1] - middle_y) for point in points)
    denominator = sum((point[0] - middle_x) ** 2 for point in points)

    a = numerator / denominator if denominator != 0 else 0
    b = middle_y - a * middle_x

    #Gib die optimalen Parameter als Tupel zurück
    return a, b

def distance_to_opt(points, lines):
    #Berechne die optimale Gerade
    optimal_line = get_optimal_line(points)

    #Berechne den quadratischen Abstand der optimalen Linie
    optimal_distance = get_linedistance(points, optimal_line)

    #Initialisiere die Differenz mit einem großen Wert damit erster gefundener Wert automatisch der neue kleinste Vergleichswert ist
    min_difference = float('inf')

    #Iteriere über die gegebenen Geraden
    for line in lines:
        #Berechne den quadratischen Abstand für die aktuelle Linie
        current_distance = get_linedistance(points, line)

        #Berechne die Differenz mit dem quadratischen Abstand der optimalen Linie mithilfe der Betragsfunktion abs()
        difference = abs(current_distance - optimal_distance)

        #Aktualisiere den minimalen Unterschied, falls es nötig sein sollte
        min_difference = min(min_difference, difference)

    #Gib die Differenz zurück
    return min_difference


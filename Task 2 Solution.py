def get_lattice_point_number(P, Q, T):


    #Variablentupel auch in dieser Funktion definieren(Versuch vllt klappts)
    p1, p2 = P
    q1, q2 = Q
    t1, t2 = T


    # Prüfen, ob eine der Koordinaten von T negativ ist
    if any(t_1_t_2 < 0 for t_1_t_2 in T):
        return 'Die Eingabe ist fehlerhaft.'

    # Überprüfen, ob der Schnitt der Rechtecke leer ist
    if intersects((min(p1, q1),min(p2, q2)), (max(p1, q1), max(p2, q2)), (t1, t2)) is False:
        return 'Der Schnitt der gegebenen Rechtecke ist leer.'

    L = (get_delta_x1(min(p1, q1), max(p1, q1), t1) + 1) * (get_delta_x2(min(p2, q2), max(p2, q2), t2) + 1)#iwas stimmt hier nicht!!!!
    #es sollte 4 rauskommen es kommt aber 6 raus also muss irgendwo wo eig 1rauskommen sollte in x1 oder x2 hier 2 rauskommen prüfen!!!

    return f'Die Anzahl der Gitterpunkte im Rechteck betraegt {L}.'

def get_delta_x1(p1, q1, t1):
    # Minimum und Maximum der x-Koordinaten
    x_min = min(p1, q1)
    x_max = max(p1, q1)

    if x_min > 0:
        return min(x_max, t1) - x_min
    else:
        return min(x_max, t1)

        # Berechnen der y-Seitenlänge des Schnitts p2 ist nun y_min und q2 is y_max

def get_delta_x2(p2, q2, t2):
    # Minimum und Maximum der y-Koordinaten
    y_min = min(p2, q2)
    y_max = max(p2, q2)
    if y_min > 0:
        return min(y_max, t2) - y_min
    else:
        return min(y_max, t2)

    # Berechnen der Anzahl der Gitterpunkte im Schnitt durch simple Multiplikation allerdings muss man beachten, dass
    # Strecken der Länge 3 vier Gitterpunkte besitzen, deswegen +1 jeweils




#Gibt uns Koordinaten der unteren linken und oberen rechten Ecke durch vergleichen der Werte
#P = (p1, p2) und Q = (q1, q2)
def convert_to_standard(P, Q):
    p1, p2 = P
    q1, q2 = Q

    #Minimum und Maximum der x-Koordinaten
    x_min = min(p1, q1)
    x_max = max(p1, q1)

    #Minimum und Maximum der y-Koordinaten
    y_min = min(p2, q2)
    y_max = max(p2, q2)

    #Ergebnistupel
    result = (x_min,y_min),(x_max,y_max) #neues P, neues Q

    return result

# Überprüfen, ob der Schnitt der Rechtecke nicht leer ist
#!!!!!Es sollte ggf. leichter sein die Fälle in den sich die Rechtecke in Standardform nicht schneiden zu charakterisieren.!!!!!!
def intersects(P, Q, T):
    p1, p2 = P
    q1, q2 = Q
    t1, t2 = T
    # Minimum und Maximum der x-Koordinaten
    p1 = min(p1, q1)
    q1 = max(p1, q1)

    # Minimum und Maximum der y-Koordinaten
    p2 = min(p2, q2)
    q2 = max(p2, q2)
#4 Hauptbedingungen sodass p in jedem quadranten liegt, bedenke q ist immer rechts über p

    if p2 > t2:
        return False

    elif p1 > t1:
        return False

    elif q1 < 0:
        return False

    elif q2 < 0:
        return False


    return True #falls keine bedingung hittet



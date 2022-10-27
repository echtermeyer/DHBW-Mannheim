# Generell: Spieler 1 und Spieler x sind synonym zu verwenden, je nach Anwendungsfall wird das jeweilige genommen
# Generell: Spieler 2 und Spieler o sind synonym zu verwenden, je nach Anwendungsfall wird das jeweilige genommen

# Hier die Anleitung:
# Spieler x und o spielen abwechselnd, Spieler x beginnt
# Um ein Feld zu wählen, muss die Koordinate des Feldes eingegeben werden.
# Diese Koordinate beginnt jeweils bei 0. Das Feld oben links hat daher die Koordinaten: 00
# Beachte: Bitte die beiden Koordinaten zusammen eingeben, z.B. 00 oder 12 oder 21
# Das Spiel endet mit dem Sieg eines Spielers oder einem Unentschieden

from typing import List


# Funktion zur Darstellung des Spielfeldes
def draw_grid(grid: List[List[int]]) -> None:
    # Für jeden Eintrag in grid wird das zugehörige Zeichen ausgegeben
    for row in range(len(grid)):
        for column in range(len(grid[row])):

            end_symbol = "┃" if column < 2 else ""

            if grid[row][column] == 1:
                print(" x ", end=end_symbol)
            elif grid[row][column] == -1:
                print(" o ", end=end_symbol)
            else:
                print("   ", end=end_symbol)

        if row < 2:
            print("\n━━━━━━━━━━━")
    print()


# Funktion zur Überprüfung des Ergebnisses
def is_finished(grid: List[List[int]], moves: int) -> bool:
    # Spieler 1 wird überprüft. Wenn die Summe 3 ist, dann hat er gewonnen
    #            (da für Spieler 1 eine 1 in grid eingefügt wird):
    # Spieler 1, wenn eine horizontale Reihe hat
    if (sum(grid[0]) == 3) or (sum(grid[1]) == 3) or (sum(grid[2]) == 3):
        print("Player x hat gewonnen!")
        return True

    # Spieler 1, wenn er eine vertikale Reihe hat
    elif grid[0][0] + grid[1][0] + grid[2][0] == 3:
        print("Player x hat gewonnen!")
        return True
    elif grid[0][1] + grid[1][1] + grid[2][1] == 3:
        print("Player x hat gewonnen!")
        return True
    elif grid[0][2] + grid[1][2] + grid[2][2] == 3:
        print("Player x hat gewonnen!")
        return True

    # Spieler 1, wenn er eine diagonale Reihe hat
    elif (grid[0][0] + grid[1][1] + grid[2][2]) == 3:
        print("Player x hat gewonnen!")
        return True
    elif (grid[0][2] + grid[1][1] + grid[2][0]) == 3:
        print("Player x hat gewonnen!")
        return True

    # Spieler 2 wird überprüft. Wenn die Summe -3 ist, dann hat er gewonnen
    #            (da für Spieler 2 eine -1 in grid eingefügt wird):
    # Spieler 2, wenn eine horizontale Reihe hat
    elif (sum(grid[0]) == -3) or (sum(grid[1]) == -3) or (sum(grid[2]) == -3):
        print("Player o hat gewonnen!")
        return True

    # Spieler 2, wenn er eine vertikale Reihe hat
    elif grid[0][0] + grid[1][0] + grid[2][0] == -3:
        print("Player o hat gewonnen!")
        return True
    elif grid[0][1] + grid[1][1] + grid[2][1] == -3:
        print("Player o hat gewonnen!")
        return True
    elif grid[0][2] + grid[1][2] + grid[2][2] == -3:
        print("Player o hat gewonnen!")
        return True

    # Spieler 2, wenn er eine diagonale Reihe hat
    elif (grid[0][0] + grid[1][1] + grid[2][2]) == -3:
        print("Player o hat gewonnen!")
        return True
    elif (grid[0][2] + grid[1][1] + grid[2][0]) == -3:
        print("Player o hat gewonnen!")
        return True

    # Wenn keiner eine Reihe hat und die 9 Züge vorbei sind, ist es ein Unentschieden
    elif moves == 9:
        print("Das ist ein Unentschieden!")
        return True

    # Wenn keine der vorangegangenen Bedingungen erfüllt ist, geht das Spiel weiter
    else:
        return False


# Funktion zur Eingabe von neuen Zügen
def enter_input(grid: List[List[int]], turn: int) -> List[List[int]]:
    # User Eingabe mit input()
    print()
    print("################################")

    # Schleife bis zur gültigen Eingabe
    not_valid = True
    while not_valid:

        # Den Spielern sagen, wer dran ist.
        rc = input("Player {} ist dran: ".format("x" if turn == 1 else "o")).strip()

        # Das erste und letzte Zeichen der Eingabe wählen
        row = rc[0]
        column = rc[-1]

        # Überprüfen, ob es sich um Zahlen handelt
        if row.isdigit() and column.isdigit():
            row = int(row)
            column = int(column)

            # Falls die Zahlen nicht im grid sind oder bereits belegt sind, dann while wiederholen
            if not 0 <= row <= 2 or not 0 <= column <= 2:
                print("Feld nicht vorhanden!")
            elif grid[row][column] != 0:
                print("Feld bereits belegt!")
            else:
                break
        else:
            print("Keine gültige Eingabe!")
    print("################################")
    print()

    # Den grid updaten mit der jeweiligen Zahl von dem aktuellen Spieler
    grid[row][column] = turn

    # Den neuen grid zurückgeben
    return grid


def main() -> None:
    # Anleitung für Spieler
    print("\n################################")
    print("Willkommen bei TikTakToe!\n")
    print("Hier die Anleitung: ")
    print("Spieler x und o spielen abwechselnd, Spieler x beginnt.")
    print("Um ein Feld zu wählen, muss die Koordinate des Feldes eingegeben werden.")
    print("Diese Koordinate beginnt jeweils bei 0. Das Feld oben links hat daher die Koordinaten: 00")
    print("Beachte: Bitte die beiden Koordinaten hintereinander eingeben, z.B. 00 oder 12 oder 21")
    print("\nViel Spaß!")
    print("################################\n")

    # Initialisierung der benötigten Variablen
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    moves = 0  # Wie viele Züge sind bereits genommen worden
    turn = 1  # Wer ist dran? 1 für Player X und -1 für Player O

    # Schleife bis Spiel beendet ist (is_finished ist dann True)
    while not is_finished(grid, moves):
        # grid wird gezeichnet
        draw_grid(grid)
        # grid wird updated durch die Eingaben
        grid = enter_input(grid, turn)

        # Nun ist der andere Spieler an der Reihe
        if turn == 1:
            turn = -1
        else:
            turn = 1

        # Die Anzahl der Züge steigt um 1
        moves += 1

    # Abschließend nochmal den beendeten grid ausgeben
    print()
    draw_grid(grid)


if __name__ == "__main__":
    main()

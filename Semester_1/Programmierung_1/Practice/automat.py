import time
from random import randrange


# IMPORTANT NOTES: Ich habe die Kommentare mit Absicht kurz und übersichtlich gehalten, um
#                  die Lesbarkeit des Codes sicherzustellen.

# Diese Funktion ist für den gesamten Automaten zuständig
def start_automat(prices, products):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Herzlich Willkommen bei unserem Shop, wir freuen uns, dass du da bist!\n")

    # Formatierung der Cents in Euro
    print("Der {} kostet heute {:.2f}€".format(products[0], prices[0] / 100))
    print("Das {} kostet heute {:.2f}€".format(products[1], prices[1] / 100))

    # Wiederholt sich, bis ein gültiges Gericht gewählt wurde
    valid = False
    while not valid:
        product_index = input("\nUm den Bierkasten zu wählen, geben Sie 0 ein und für das Tagesgericht 1:  ")

        if product_index == "0" or product_index == "1":
            product_index = int(product_index)
        else:
            print("Leider ist dieses Produkt nicht verfügbar. Bitte versuche es erneut.")
            continue

        print("\nSie haben Produkt {} gewählt.".format(products[product_index]))
        valid = ("1" == input("Ist dies korrekt? Falls richtig, geben Sie eine 1 ein, andernfalls eine 0: "))

    p = prices[product_index]
    print("\nDies hat einen Preis von {:.2f}€".format(p / 100))

    # Wiederholt sich, bis ein gültiger Betrag eingegeben wurde
    valid = False
    while not valid:
        try:
            money = float(input("Bitte geben Sie ein, welchen Geldmenge Sie zum bezahlen verwenden möchten (in €): ").replace("€", ""). \
                          strip().replace(",", ".")) * 100

            if money >= p:
                valid = True
            else:
                print("Das ist leider zu wenig :(")
        except:
            print("Bitte geben Sie einen validen Betrag an!")
            continue

    diff = int(money - p)

    # Berechnung der Anzahl der Kupfermünzen
    # Floor Division (und Aneinanderreihung) für 5 Cent und 2 Cent
    # 2x Floor Division bedeutet, dass alles was übrig bleibt nach "% 2" 1 Centstücke sind (maximal 1x 1 Cent)
    amount_5 = diff // 5
    amount_2 = diff // 5 // 2
    amount_1 = diff // 5 // 2 % 2

    print("\nDu bekommst {:.2f}€ Rückgeld: ".format(diff / 100))
    print("{}x 5 Cent, {}x 2 Cent und {}x 1 Cent".format(amount_5, amount_2, amount_1))
    print("\nVielen Dank für deinen Einkauf, bis zum nächsten Mal!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Main Funktion
if __name__ == "__main__":

    # Preise werden hier gesetzt, damit der Automat ein einem Tag auch immer den gleichen Preis hat
    prices = [1299, randrange(500, 2000)]

    # Für die Produkte gilt das gleiche wie für die Preise
    products = ["Bierkasten", "Tagesgericht"]

    # Der Automat soll öfters pro Tag verwendet werden. Nachdem er ausgeschaltet wird, wird auch die Schleife gestoppt.
    while True:
        start_automat(prices, products)

        # Nach 5 Sekunden startet der Automat von neu und kann vom nächsten Kunden benutzt werden
        time.sleep(5)

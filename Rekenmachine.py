from io import StringIO
import time
import os

# Rekenmachine Python Programma gemaakt door Joaquin Goossens (Snesseye)

print("Programma opstarten...")
time.sleep(2)
print("Rekenmachine geladen.")
time.sleep(1)
naam = str(input("Van wie is dit rekenmachine? -> "))
print("Hallo",naam,"en welkom bij jouw persoonlijke rekenmachine.")
time.sleep(1)
print("Wat zou je graag willen doen?")
methode = input("Optellen / Aftrekken / Delen / Vermenigvuldigen -> ")
clearConsole = lambda: print('\n' * 150)
clearConsole()

# Optellen

if methode == "Optellen":
    print("We gaan beginnen met optellen.")
    time.sleep(1)
    print("Ik heb 2 getallen van je nodig.")
    time.sleep(1)
    print("Typ het eerste getal aub.")
    optellen_1 = int(input())
    print("Dankje! Typ nu het tweede getal aub.")
    optellen_2 = int(input())
    print("Top, ontvangen. Even berekenen...")
    optellen_uitkomst = optellen_1 + optellen_2
    time.sleep(2)
    print("De uitkomst is", optellen_uitkomst)

# Aftrekken

if methode == "Aftrekken":
    print("We gaan beginnen met aftrekken.")
    time.sleep(1)
    print("Ik heb 2 getallen van je nodig.")
    time.sleep(1)
    print("Typ het eerste getal aub.")
    aftrekken_1 = int(input())
    print("Dankje! Typ nu het tweede getal aub.")
    aftrekken_2 = int(input())
    print("Top, ontvangen. Even berekenen...")
    aftrekken_uitkomst = aftrekken_1 - aftrekken_2
    time.sleep(2)
    print("De uitkomst is", aftrekken_uitkomst)

# Delen

if methode == "Delen":
    print("We gaan beginnen met delen.")
    time.sleep(1)
    print("Ik heb 2 getallen van je nodig.")
    time.sleep(1)
    print("Typ het eerste getal aub.")
    delen_1 = int(input())
    print("Dankje! Typ nu het tweede getal aub.")
    delen_2 = int(input())
    print("Top, ontvangen. Even berekenen...")
    delen_uitkomst = delen_1 / delen_2
    time.sleep(2)
    print("De uitkomst is", delen_uitkomst)

# Vermenigvuldigen

if methode == "Vermenigvuldigen":
    print("We gaan beginnen met vermenigvuldigen.")
    time.sleep(1)
    print("Ik heb 2 getallen van je nodig.")
    time.sleep(1)
    print("Typ het eerste getal aub.")
    vermenigvuldigen_1 = int(input())
    print("Dankje! Typ nu het tweede getal aub.")
    vermenigvuldigen_2 = int(input())
    print("Top, ontvangen. Even berekenen...")
    vermenigvuldigen_uitkomst = vermenigvuldigen_1 * vermenigvuldigen_2
    time.sleep(2)
    print("De uitkomst is", vermenigvuldigen_uitkomst)
osszeg = 0
darab = 0

while True:
    magassag = int(input("Adjon meg egy testmagasságot cm-ben: "))
    osszeg += magassag
    darab += 1
    if magassag <= 0 or magassag >= 250:
        break

atlag = round(osszeg / darab, 1)
print(f"Az átlagmagasság az {atlag}")
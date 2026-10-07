import math

szelesseg = 0
magassag = 0

while szelesseg <= 0 or magassag <= 0:
    szelesseg = float(input("Adja meg a téglalap szélességét: "))
    magassag = float(input("Adja meg a téglalap magasságát: "))

kerulet = 2 * (magassag + szelesseg)
terulet = magassag * szelesseg
atlo = math.sqrt(magassag ** 2 + szelesseg ** 2)

print(f"A téglalap kerülete {kerulet} cm, területe {terulet} cm2, átlója {atlo:.2f} cm.")
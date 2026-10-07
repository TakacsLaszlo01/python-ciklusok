import math
r = 0
while r <= 0:
    r = float(input("Adja meg a kör sugarát: "))

d = 2 * r
kerulet = round(d * math.pi, 2)
terulet = round(r ** 2 * math.pi, 2)

print(f"A kör átmérője {d} cm, a kerülete {kerulet} cm, a területe pedig {terulet} cm2.")
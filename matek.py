import math

gyok = math.sqrt(2)
print(gyok)

befogo_a = float(input("Adja meg az egyik befogó hosszát: "))
befogo_b = float(input("Adja meg a másik befogó hosszát: "))

atfogo = math.sqrt(befogo_a * befogo_a + befogo_b * befogo_b)
print(f"Az átfogó hossza {atfogo}.")

#kerekítések
pi = math.pi
kerekitett = round(pi, 4)
print(f"A pí 4 tizedesjegyre kerekítve {kerekitett}")

#plafon és padló
x = 0
while x <= 0:
    x = float(input("Adjon meg egy pozitív számot: "))

plafon = math.ceil(x)
print(f"Felfelé kerekítés eredménye: {plafon}")
padlo = math.floor(x)
print(f"Lefelé kerekítés eredménye: {padlo}")
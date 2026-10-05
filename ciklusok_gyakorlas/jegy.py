osszeg = 0
darab = 0
jegy = 1

print("Adjon meg 1 és 5 közötti érdemjegyeket. A 0-val tud kilépni a programból.")
while 1 <= jegy <= 5:
    jegy = int(input("Adjon meg egy érdemjegyet: "))
    osszeg += jegy
    darab += 1

atlag = osszeg / darab
print(f"A tanulmányi átlag {atlag}")
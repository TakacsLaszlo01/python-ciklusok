nev_hossza = 0
while nev_hossza < 6:
    nev = input("Adjon meg egy legalább 6 karakteres felhasználónevet:  ")
    nev_hossza = len(nev)

osztalyzat = 0
while not (1 <= osztalyzat <= 5) or osztalyzat % 1 != 0:
    osztalyzat = int(input("Adjon meg egy osztályzatot, ami 1-től 5-ig lehet egy egész szám: "))
    

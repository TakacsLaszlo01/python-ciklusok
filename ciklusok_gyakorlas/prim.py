n = int(input("Adjon meg egy természetes számot: "))

if n <= 0:
    print("Csak pozitív egész lehet prím!")
else:
    i = 2
    while i < n and n % i != 0:           
         i += 1
         
    if i == n:
        print(f"{n} egy prím!") 
    else:
        print(f"{n} nem prím!")
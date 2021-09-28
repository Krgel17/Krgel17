numero = input("Pasa el numero")

cont = 0
for i in range(numero):
    if numero % i == 0:
        cont = cont + 1
        
        
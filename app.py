numero = int (input("Pasa el numero: "))

cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont = cont + 1
        
if cont ==2:
    print("El numero ",numero," es primo")
else:
    print("El numero ",numero," no es primo")
    
    #Comentarios
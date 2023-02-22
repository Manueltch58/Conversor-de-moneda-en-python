valor = int(input("Ingrese el valor que quiere convertir: "))

dolar = 4610
euro = 4467
yen = 32
libra = 5111
rublo = 72
bitcoin = 88232500


opcion = 0
while True:
    print("""
    ¿qué quieres hacer?
    
    1) Dolar a COP
    2) Euro a COP
    3) Yen a COP
    4) Libra a COP
    5) Rublo a COP
    6) Bitcoin a COP
    7) Reiniciar
    8) Apagar conversor
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("$",valor,"Dólares es igual a",dolar*valor,"pesos")
    
    elif opcion == 2:
        print(" ")
        print("€",valor,"Euros es igual a",euro*valor,"pesos")
    
    elif opcion == 3:
        print(" ")
        print("¥",valor,"Yenes es igual a",yen*valor,"pesos")
        
    elif opcion == 4:
        print(" ")
        print("£",valor,"Libras es igual a",libra*valor,"pesos")
        
    elif opcion == 5:
        print(" ")
        print("₽",valor,"Rublos es igual a",rublo*valor,"pesos")
        
    elif opcion == 6:
        print(" ")
        print("฿",valor,"Bitcoic es igual a",bitcoin*valor,"pesos")
    
    elif opcion == 7:
        
        valor = int(input("Ingrese el nuevo valor ") )
    
    elif opcion == 8:
        print("¡hasta luego!")
        break
    
    else:
        print("Pongase serio")
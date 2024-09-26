while True:
    while True:
        a = int(input('Introduzca un año entre 1900 y 2199: '))
        cuenta = 0
        if 1900 <= a <= 2199:
            for i in range(1900,a):
                if i % 4 == 0 and (i % 400 != 0 or i % 100 == 0):
                    cuenta += 1

            print(f"La cantidad de años bisiestos entre 1900 y {a} es de {cuenta}")
            break
        else:
            print('Introduzca un año valido!!!')
        
    
    sal = int(input("""Desea realizar el proceso con otro numero?
NO = 0
SI = 1 \n"""))
    if sal == 0:
        print('El programa a terminado.')
        quit()
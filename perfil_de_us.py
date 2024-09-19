print('Hola, Soy el profesor Oak!')
genero = input('Eres un chico o una chica? ')
 
if genero == "chico":
    print('Bienvenido!')
else:
    print('Bienvenida!')

edad = input('Cual es tu edad? ')
if int(edad)<10:
    r = 'NO tienes edad para ser entrenador'
    if genero == 'chica' :
         r += 'a' 
         print(r)
    else:
         print(r)
    quit()
else:
    print('Tu aventura ya comenzara')

region = input('De cual region vienes?')
if region == 'Kanto'


tipo = input('Que tipo de pokemon deseas fuego, planta, agua.')
if tipo == 'fuego':
    print('Tu starter es Cyndaquil')
elif tipo == 'planta' :
    print('Tu starter es Rowlet')
elif tipo == 'planta':
    print('Tu starter es Oshawot')
else:
    print('Debes elegir fuego, agua, planta  ')
    quit()
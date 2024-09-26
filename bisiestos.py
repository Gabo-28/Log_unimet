# Pedir al usuario un año
a = int(input("Introduce un año entre 1900 y 2199: "))

# Validar el año ingresado
if 1900 <= a <= 2199:
    # Calcular cantidad de años bisiestos desde 1900 hasta year_input
    bisiestos_hasta_a = (a // 4) - (a // 100) + (a // 400)
    bisiestos_hasta_1899 = (1899 // 4) - (1899 // 100) + (1899 // 400)
    cantidad_bisiestos = bisiestos_hasta_a - bisiestos_hasta_1899
    
    print(f"Cantidad de años bisiestos desde 1900 hasta {a}: {cantidad_bisiestos}")
else:
    print("Año fuera de rango. Por favor, introduce un año entre 1900 y 2199.")
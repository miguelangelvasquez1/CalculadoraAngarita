def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Introduce tu opción (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")
            elif opcion == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")
            elif opcion == '3':
                print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

        siguiente = input("¿Quieres realizar otra operación? (s/n): ")
        if siguiente.lower() != 's':
            break

calculadora()

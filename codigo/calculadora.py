def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero no permitida"

def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Introduce tu elección (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {suma(num1, num2)}")

        elif opcion == '2':
            print(f"Resultado: {resta(num1, num2)}")

        elif opcion == '3':
            print(f"Resultado: {multiplicacion(num1, num2)}")

        elif opcion == '4':
            print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
calculadora()
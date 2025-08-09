print("=== CALCULADORA ===")
print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingresa el número de la operación (1/2/3/4): ")

opcion = input("Ingresa el número de la operación (1/2/3/4): ")

if opcion in ["1", "2", "3", "4"]:
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))

    if opcion == "1":
        resultado = num1 + num2
        operacion = "Suma"
    elif opcion == "2":
        resultado = num1 - num2
        operacion = "Resta"
    elif opcion == "3":
        resultado = num1 * num2
        operacion = "Multiplicación"
    elif opcion == "4":
        if num2 != 0:
            resultado = num1 / num2
            operacion = "División"
        else:
            resultado = "Error: No se puede dividir por cero."
            operacion = "División"

    print(f"\nResultado de la {operacion}: {resultado}")
else:
    print("Opción inválida. Debes ingresar 1, 2, 3 o 4.")
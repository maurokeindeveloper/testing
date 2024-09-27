from src import calculator 

def main():
    num1 = float(input("Escribí el primer número: "))
    num2 = float(input("Escribí el segundo número: "))
    operator = input("Ingresá el operador (+, -, *, /)")
    result = calculator.calculate(num1,num2,operator)
    print(f"El resultado es: {result}")
    
if __name__ == "__main__":
    main()
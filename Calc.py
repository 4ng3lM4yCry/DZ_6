import sys

def calculate(num1, num2, operation):
    """
    Выполняет арифметическую операцию над двумя числами..
    
    Аргументы:
        num1 (float): Первое число
        num2 (float): Второе число
        operation (str): Операция (+, -, *, /)
    
    Возвращает:
        float: Результат вычисления или None в случае ошибки
    """
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: Деление на ноль!")
                return None
            return num1 / num2
        else:
            print(f"Ошибка: Неизвестная операция '{operation}'")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def main():
    """Основная функция программы."""
    print("=== ПРОСТОЙ КАЛЬКУЛЯТОР ===\n")
    
    # Проверка аргументов командной строки
    if len(sys.argv) == 4:
        # Использование аргументов командной строки
        try:
            num1 = float(sys.argv[1])
            operation = sys.argv[2]
            num2 = float(sys.argv[3])
            
            result = calculate(num1, num2, operation)
            if result is not None:
                print(f"Результат: {num1} {operation} {num2} = {result}")
        except ValueError:
            print("Ошибка: Аргументы должны быть числами!")
            print("Использование: python calculator.py <число1> <операция> <число2>")
    else:
        # Интерактивный режим
        print("Введите 'exit' для выхода.")
        print("Доступные операции: +, -, *, /")
        
        while True:
            try:
                # Ввод первого числа
                input1 = input("\nВведите первое число: ").strip()
                if input1.lower() == 'exit':
                    print("Выход из программы...")
                    break
                
                # Ввод операции
                operation = input("Введите операцию (+, -, *, /): ").strip()
                if operation.lower() == 'exit':
                    print("Выход из программы...")
                    break
                
                # Ввод второго числа
                input2 = input("Введите второе число: ").strip()
                if input2.lower() == 'exit':
                    print("Выход из программы...")
                    break
                
                # Преобразование в числа и вычисление
                num1 = float(input1)
                num2 = float(input2)
                
                result = calculate(num1, num2, operation)
                if result is not None:
                    print(f"Результат: {num1} {operation} {num2} = {result}")
                    
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректные числа!")
            except KeyboardInterrupt:
                print("\n\nВыход из программы...")
                break
            except EOFError:
                print("\n\nВыход из программы...")
                break

if __name__ == "__main__":

    main()

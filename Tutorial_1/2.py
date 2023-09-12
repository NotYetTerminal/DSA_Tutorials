def calculate(num1: float, num2: float, operator: str) -> str:
    operator_dict: dict = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
    }

    if (num2 != 0):
        operator_dict['/'] = num1 / num2
        operator_dict['%'] = num1 % num2

    if (operator in operator_dict):
        return str(operator_dict[operator])
    else:
        return "Operator not found or permitted!"


if __name__ == '__main__':
    number1: float = 30
    number2: float = 20
    number_operator: str = "+"

    result: str = calculate(number1, number2, number_operator)

    print(f"{number1} {number_operator} {number2} = {result}")

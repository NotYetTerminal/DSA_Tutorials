def factorial(number_in: int) -> int:
    result: int = 1
    
    for index in range(1, number_in+1):
        result *= index
    
    return result


if __name__ == '__main__':
    number: int = 5

    result: int = factorial(number)

    print(f"{number}! = {result}")

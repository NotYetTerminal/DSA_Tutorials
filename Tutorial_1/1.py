def check(array_in: list, target_in: int) -> int:
    count: int = 0

    for number in array_in:
        if (number == target_in):
            count += 1
    
    return count


if __name__ == '__main__':
    normal_array: list = [1, 2, 3, 4, 1, 2, 7, 12, 2]
    target: int = 2
    
    result: int = check(normal_array, target)

    print(f"Target: {target}")
    print(f"{result} found in array.")

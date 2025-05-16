def main():
    user_input = input("Введите числа через запятую: ")
    numbers = list(map(int, user_input.split(',')))


    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Четные числа: {even_numbers}")

    max_num = max(numbers)
    min_num = min(numbers)
    print(f"Максимальное число: {max_num}")
    print(f"Минимальное число: {min_num}")


    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(f"Отсортированный список: {numbers}")

if __name__ == "__main__":
    main()

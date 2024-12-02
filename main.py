# ДЗ: Применение условий


def sum_even():
    summary = 0
    for i in range(0, 100, 2):
        summary += i
    return summary


def count_entry():
    num = 0
    counter = 0

    while num >= 0:
        try:
            num = int(input("Введите положительное число: "))
        except ValueError:
            print("Введено некорректное число, попробуйте еще раз")
        else:
            counter += 1

    return counter


odd_numbers = [i ** 2 for i in range(1, 10) if i % 2 != 0]


def main():
    print(f"Сумма всех четных чисел от 0 до 100: {sum_even()}")
    print(f"Квадраты всех нечетных чисел от 1 до 10: {odd_numbers}")
    print(f"Количество введенных чисел: {count_entry()}")


main()

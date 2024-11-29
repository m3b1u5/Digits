# ДЗ: Применение условий

odd_numbers = [i ** 2 for i in range(1, 10) if i % 2 != 0]


def sum_even():
    summary = 0
    for i in range(0, 100, 2):
        summary += i
    return summary


def main():
    num = 0
    counter = 0

    while num >= 0:
        try:
            num = int(input("Введите положительное число: "))
        except ValueError:
            print("Введено некорректное число, попробуйте еще раз")
        else:
            counter += 1

    print(f"Количество введенных чисел: {counter}")


main()

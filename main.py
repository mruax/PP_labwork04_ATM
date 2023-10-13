def hundred_numbers(a, flag):
    num = str(a)
    res = ""
    if len(num) == 3:
        res += three_digit[int(num[0]) * 100] + " "
        num = str(int(num[1:]))
    t = int(num)
    if t in number_alphabet:
        if t in [1, 2] and flag:
            res += thousand_amount[t - 1] + " "
        else:
            res += number_alphabet[t] + " "
    else:
        res += two_digit[int(num[-2]) * 10] + " "
        if t in [1, 2] and flag:
            res += thousand_amount[t - 1] + " "
        else:
            res += number_alphabet[int(num[-1])] + " "
    return res


if __name__ == "__main__":
    n = input("Введите сумму от 1 до 100000: ")
    while isinstance(n, str):
        try:
            n = int(n)
            if not (1 <= n <= 100000):
                raise Exception
        except Exception:
            n = input("Неверно! Введите сумму от 1 до 100000: ")
    # слова без склонения
    number_alphabet = {1: "один",
                       2: "два",
                       3: "три",
                       4: "четыре",
                       5: "пять",
                       6: "шесть",
                       7: "семь",
                       8: "восемь",
                       9: "девять",
                       10: "десять",
                       11: "одиннадцать",
                       12: "двенадцать",
                       13: "тринадцать",
                       14: "четырнадцать",
                       15: "пятнадцать",
                       16: "шестнадцать",
                       17: "семнадцать",
                       18: "восемнадцать",
                       19: "девятнадцать",
                       20: "двадцать",
                       0: ""
                       }
    two_digit = {20: "двадцать",
                 30: "тридцать",
                 40: "сорок",
                 50: "пятьдесят",
                 60: "шестьдесят",
                 70: "семьдесят",
                 80: "восемьдесят",
                 90: "девяносто"
                 }
    three_digit = {100: "сто",
                   200: "двести",
                   300: "триста",
                   400: "четыреста",
                   500: "пятьсот",
                   600: "шестьсот",
                   700: "семьсот",
                   800: "восемьсот",
                   900: "девятьсот"
                   }
    # склоняющиеся слова (последняя цифра = 1 // 2,3,4 // 5,6,7,8,9,0)
    thousand_amount = ["одна", "две"]
    thousands = ["тысяча", "тысячи", "тысяч"]
    rubles = ["рубль", "рубля", "рублей"]
    # число разбивается на две части ***.*** (a и b)
    result = ""
    if len(str(n)) > 3:
        a = n // 1000
        res1 = hundred_numbers(a, True)
        result += res1
        if a % 10 == 1:
            result += thousands[0] + " "
        elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
            result += thousands[1] + " "
        else:
            result += thousands[2] + " "
    b = n % 1000
    res2 = hundred_numbers(b, False)
    result += res2
    if b % 10 == 1:
        result += rubles[0]
    elif b % 10 == 2 or b % 10 == 3 or b % 10 == 4:
        result += rubles[1]
    else:
        result += rubles[2]
    print(result.capitalize().replace("  ", " "))

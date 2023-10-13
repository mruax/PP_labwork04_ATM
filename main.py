import pymorphy2


if __name__ == "__main__":
    morph = pymorphy2.MorphAnalyzer()
    ans = morph.parse('рубль')[0]

    n = input("Введите сумму от 1 до 100000: ")
    while type(n) is str:
        try:
            n = int(n)
            if not(1 <= n <= 100000):
                raise Exception
        except Exception:
            n = input("Неверно! Введите сумму от 1 до 100000: ")
    print(n, ans.make_agree_with_number(n).word)

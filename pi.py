# формула Бейлия-Борвейна-Плаффа
def pi_digits():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if (4 * q + r - t) < (n * t):
            yield n
            q, r, t, k, n, l = 10 * q, 10 * (r - n * t), t, k, (10 * (3 * q + r)) // t - 10 * n, l
        else:
            q, r, t, k, n, l = q * k, (2 * q + r) * l, t * l, k + 1, (q * (7 * k + 2) + r * l) // (t * l), l + 2


digits_generator = pi_digits()
digits = [next(digits_generator) for _ in range(10)]

values = list(map(lambda x: (x / x ** 2 if x != 0 else 0) + x, digits))  # выполнение задания

for digit, value in zip(digits, values):
    print(f"Цифра: {digit}, Вычисленное значение: {value}")

# 5 Лабораторная работа Python. 4-й вариант
## Генератор цифр числа π. Поделите каждую цифру на её квадрат и найдите сумму этих значений.
Для получения цифр числа π, я воспользовался [формулой Бейлия-Борвейна-Плаффа.](https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%91%D1%8D%D0%B9%D0%BB%D0%B8_%E2%80%94_%D0%91%D0%BE%D1%80%D1%83%D1%8D%D0%B9%D0%BD%D0%B0_%E2%80%94_%D0%9F%D0%BB%D0%B0%D1%84%D1%84%D0%B0)
![image](https://github.com/user-attachments/assets/f934fb77-8c3c-491a-b167-e18f3a8f5712)
## Описание работы кода

Генератор `pi_digits()` бесконечно вычисляет и возвращает цифры числа Пи. Он начинает с инициализации некоторых переменных, а затем входит в бесконечный цикл, где происходит вычисление цифр Пи.

В каждой итерации цикла проверяется условие `4*q+r-t < n*t`. Если оно истинно, то текущее значение `n` (которое представляет собой следующую цифру Пи) возвращается с помощью оператора `yield`, а затем обновляются значения переменных для следующей итерации.
Если условие `4*q+r-t < n*t` ложно, то значения переменных обновляются без возвращения следующей цифры Пи, и цикл продолжается.

- `q`, `r`, `t` - это три переменные, которые используются для вычисления следующей цифры числа Пи. Они обновляются на каждом шаге цикла.
- `k` - это счетчик, который увеличивается на 1 на каждом шаге цикла.
- `n` - это следующая цифра числа Пи, которая будет выведена.
- `l` - это еще одна переменная, влияющая на `q`, `r`, `t`. Она также обновляется на каждом шаге цикла.

## К генератору должна быть применена хотя бы одна из функций `map`, `reduce`, `filter`.
В коде был применена функция `map` для выполнения вычислений для всех значений `x`.

[Доп. источники](https://github.com/BrolanJ/Bailey-Borwein-Plouffe/blob/master/BBP%20Formula.py)

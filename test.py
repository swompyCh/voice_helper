from time import monotonic

t = monotonic()
i = float(input("Введите время(в минутах): "))
i *= 60
b = bool('true')
f = 0
while f > 2:
    print(f)
    if monotonic() - t > i:
        t = monotonic()
        print('Время вышло')
    b = bool('false')
    print(b)
    f += 1
print("ку")

import time
timing = time.time()
b = bool(True)
i = float(input("Введите время(в минутах): "))
i *= 60
while b:
    if time.time() - timing > i:
        timing = time.time()
        print("Время вышло")
        b = bool(False)
print("Ожидайте")

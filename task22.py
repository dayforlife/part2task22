def myfunc():
    a = float(input("Введите фаренгейт для конвертации в градус цельсия: "))
    b = (a - 32) * (5 / 9)
    return b
print("По цельсию: ", myfunc())

def cels_to_fahr():
    a = float(input("Введите градус по цельсию для конвертации в фаренгейт: "))
    b = ((9/5) * a + 32)
    return b
print("По фаренгейту: ", cels_to_fahr())
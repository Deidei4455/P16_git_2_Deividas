def kaupk_aritmetika(*args: int | float, operacija="suma"):
    ress = args[0]

    for elem in args[1:]:
        if elem >= 2 and "suma" in operacija:
            ress += elem
        elif elem >= 2 and "atimtis" in operacija:
            ress -= elem
        elif elem >= 2 and "dalyba" in operacija:
            ress /= elem
        elif elem >= 2 and "daugyba" in operacija:
            ress *= elem
    return ress


ivestis = int(input("iveskite skaiciu 1: "))
ivestis1 = int(input("iveskite skaiciu 2: "))
res = kaupk_aritmetika(ivestis, ivestis1, operacija="suma")
print(f"atsakymas {res}")

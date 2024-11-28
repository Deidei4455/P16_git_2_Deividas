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


res = kaupk_aritmetika(10, operacija="suma")
print(res)

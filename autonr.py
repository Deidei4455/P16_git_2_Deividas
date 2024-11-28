def check_autonr_a(numeris: str):
    if numeris[0:3].isalpha() and numeris[3:6].isdigit() and len(numeris) == 6:
        if numeris[0:3].isupper():
            return True
        else:
            return False
    else:
        return False


res = check_autonr_a("456BMA")
print(res)

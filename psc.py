def psc():
    psc1 = input("Zadejte psc: ")
    if len(psc1) == 5:
        if psc1.isdigit():
            return True
        else:
            return False
    else:
        return False

if psc():
    print("Ok")
else:
    print("psc je spatne")
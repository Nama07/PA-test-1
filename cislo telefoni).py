def kontrolacisla():
    phone_number = input("Zadejte telefonni cislo: ")
    if len(phone_number) == 9:
        if phone_number.isdigit():
            return True
        else:
            return False
    elif len(phone_number) == 13:
        if phone_number[0] == "+" and phone_number[1:].isdigit():
            return True
        else:
            return False
    else:
        return False

if kontrolacisla():
    print("Ok")
else:
    print("telefoni cislo je spatne")
def masks_card_and_account(type_and_number: str) -> str:
    type_and_number.split()
    numbers = []
    names = []
    for i in type_and_number:
        if i.isalpha():
            names.append(i)
        else:
            numbers.append(i)
    
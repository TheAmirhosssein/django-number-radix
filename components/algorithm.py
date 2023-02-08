def number_to_alphabet(number):
    if number < 10:
        return number
    elif number == 10:
        return "A"
    elif number == 11:
        return "B"
    elif number == 12:
        return "C"
    elif number == 13:
        return "D"
    elif number == 14:
        return "E"
    elif number == 15:
        return "F"
    elif number == 16:
        return "G"
    elif number == 17:
        return "H"
    elif number == 18:
        return "I"
    elif number == 19:
        return "J"


def convert_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def encrypt(number, radix):
    changed_number = []
    while number > (mod := 0):
        mod = number % radix
        mod = number_to_alphabet(mod)
        number = number // radix
        changed_number.append(mod)
    return changed_number.reverse()

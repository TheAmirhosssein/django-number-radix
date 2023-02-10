def list_reverse(lst):
    new_lst = lst[::-1]
    return new_lst


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


def alphabet_to_number(number):
    if number == "A":
        return 10
    elif number == "B":
        return 11
    elif number == "C":
        return 12
    elif number == "D":
        return 13
    elif number == "E":
        return 14
    elif number == "F":
        return 15
    elif number == "G":
        return 16
    elif number == "H":
        return 17
    elif number == "I":
        return 18
    elif number == "J":
        return 19
    else:
        return number


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


def decrypt(number, radix):
    number_sum, start = 0, 0
    for i in list_reverse(number):
        i = alphabet_to_number(i)
        number_sum += int(i) * radix**start
        start += 1
    return number_sum

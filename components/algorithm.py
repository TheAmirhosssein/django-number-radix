number = int(input(": "))
radix = int(input(": "))


def encrypt(number, radix):
    changed_number = []
    while number > (mod := 0):
        mod = number % radix
        number = number // radix
        changed_number.append(mod)
    return changed_number.reverse()

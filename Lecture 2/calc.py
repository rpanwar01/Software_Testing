def evaluate_single_digit(s):
    i = "0123456789".index(s)
    return i

def evaluate_positive_number(s):
    n = 0
    for c in s:
        d = evaluate_single_digit(c)
        n = n * 10 + d
    return n

def evaluate_floating_point_number(s):
    in_decimal = False
    n = 0
    v = 0.1
    for c in s:
        if c == '.':
            if in_decimal:
                raise ValueError("Can't have two decimal points in one number")
            else:
                in_decimal = True
            continue
        if not in_decimal:
            d = evaluate_single_digit(c)
            n = n * 10 + d
        else:
            d = evaluate_single_digit(c)
            n = n + d * v
            v = v / 10
    return n

def evaluate_single_hexadecimal_digit(s):
    i = "0123456789ABCDEF".index(s)
    return i

def evaluate_hexadecimal(s):
    n = 0
    for c in s:
        if c in "0123456789ABCDEF":
             n = n * 16 + evaluate_single_hexadecimal_digit(c)
    return n

def evaluate(s):
    if s.startswith("-"):
        return evaluate(s[1:]) * -1
    if s.startswith("0x"):
        return evaluate_hexadecimal(s[2:].upper())
    return evaluate_floating_point_number(s)

if __name__ == "__main__":
    pass
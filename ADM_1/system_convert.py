def get_code(a):
    if a.isdigit():
        return int(a)
    else:
        return int(ord(a) - ord('A') + 10)


def convert_n_to_10(a, b):
    int(b)
    pow = 1
    result = 0
    for i in a[::-1]:
        result += get_code(i) * pow
        pow *= b
    return result


def recover_code(e):
    if int(e) <= 9:
        return str(e)
    else:
        return chr(int(e) - 10 + ord('A'))


def convert_10_to_n(a, b):
    int(a)
    int(b)
    ans = ""
    while (a > 0):
        ans = recover_code(str(a % b)) + ans
        a //= b
    return ans


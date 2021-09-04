def check_number(n):
    if n >= 2:
        if n == 2:
            return True
        for j in range(2, n):
            if n % j == 0:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    r = {}
    for i in range(1, 10):
        r[i] = check_number(i)

    for k, v in r.items():
        print(k, v)

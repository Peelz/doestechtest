def is_prime(n):
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
        r[i] = is_prime(i)

    for k, v in r.items():
        print(k, v)
    """
    Result 
    1 False
    2 True
    3 False
    4 False
    5 False
    6 False
    7 False
    8 False
    9 False
    """

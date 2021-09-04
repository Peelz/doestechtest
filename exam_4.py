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


def sum_prime_number(n):
    r = {}
    for i in range(1, max_value + 1):
        a = is_prime(i)
        r[i] = a
    a = 0
    for k, v in r.items():
        if v:
            a += k
    return a


if __name__ == '__main__':
    max_value = 5
    print(sum_prime_number(5))

def func(n):
    result = 0
    for i in range(1, n + 1):
        print(i)
        if i % 2 == 0:
            result += i
        else:
            result += i * 2
    return result


if __name__ == '__main__':
    r = func(10)
    print(r)  # 80

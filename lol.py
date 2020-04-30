def fib(n):
    a = [0, 1]
    if (n <= 1):
        return n
    else:
        for i in range(2, n+1):
            a.append((a[i - 1] + a[i - 2]) % 10)
    return a[len(a) - 1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
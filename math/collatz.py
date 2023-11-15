def collatz(a):
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
    return a


max_value = 741852639645464514715623
for n in range(1, max_value + 1):
    print(n, collatz(n))

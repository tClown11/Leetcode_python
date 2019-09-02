def nihao(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return b


s = nihao(10)
print(s)

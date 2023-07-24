for i in range(1,600):
    x = bin(i)[2:]
    x = x[::-1]
    x = x + str(x.count('1')%2)
    x = int(x, 2)
    if x > 1488:
        print(i)

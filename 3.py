for i in range(1,200):
    num = i
    x = ''
    while num:
        x += str(num%3)
        num //= 3
    x = x[::-1]
    x = x.replace('2','1')
    x = x.replace('0','2')
    x = int(x,3)
    if x == 17:
        print(i)
        break

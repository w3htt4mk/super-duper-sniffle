c = 0
for i in range(100,1000):
    x = oct(i)[2:]
    if x.count('3')%2==0:
        x = x + '5'
    else:
        x = x + '6'
    x = int(x,8)
    if x % 10 == 9:
        c += 1
print(c)

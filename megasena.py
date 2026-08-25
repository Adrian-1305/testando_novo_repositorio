import random
for b in range(1,7):
    a = random.randrange(1,100)
    print (b,' = ',a, end=', ')
    if a==10 or a==7 or a==23 or a==30:
        break
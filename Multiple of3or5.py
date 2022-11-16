sums = 0
exist = []
for i in range(1,1000):
    if i%3 == 0 or i %5 == 0 and i not in exist:
        exist.append(i)
        sums += i

print(sums)

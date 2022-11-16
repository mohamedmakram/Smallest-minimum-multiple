nums = range(2,21)
div = 1
div_nums = []

def is_prime(x):
    if (x == 2) or (x == 3):
        return True
    if (x == 1) or (x % 2 == 0):
        return False
    
    for i in range(3, x // 2, 2):
        if x % i == 0:
            
            return False
    
    return True

for i in nums:
    if is_prime(i):
        div *= i
        div_nums.append(i)
        continue
    temp = i
    for j in range(len(div_nums)):
        if i % div_nums[j] == 0:
            temp = temp // div_nums[j]
        if temp == 0:
            break
        if temp != 1 and j == len(div_nums)-1:
            div_nums.append(temp)
            div *= temp


print(div)
        



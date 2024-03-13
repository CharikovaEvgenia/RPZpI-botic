import random

list = [random.randint(0, 100) for _ in range(16)]
print(list)

for index, number in enumerate(list): 
    if((index+1)%4 == 0):
        list[index] = number ** 2
        print(number)
print(list)

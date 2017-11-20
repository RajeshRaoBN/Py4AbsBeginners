import random
count = 0
heads = 0
tails = 0
while count < 100 :
    count += 1
    rand = random.randint(1,2)
    if rand == 1 :
        heads += 1
    else:
        tails += 1
print("Heads = " + str(heads))
print("Tails = " + str(tails))
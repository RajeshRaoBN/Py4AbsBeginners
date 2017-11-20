import random
li = ["we", "the", "people", "of", "Australia"]
sen = ""
le = len(li)
for i in range(0, le) :
    print(len(li))
    ran = random.randint(0,len(li)- 1)
    word = li[ran]
    sen += word
    sen += " "
    del li[ran]
print(sen)

